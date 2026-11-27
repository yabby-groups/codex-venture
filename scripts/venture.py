"""Production scheduler, service supervisor and management CLI."""
import argparse
import fcntl
import hashlib
import json
import os
import shutil
import signal
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from datetime import datetime
from decimal import Decimal
from pathlib import Path

import venture_queue as queue
from collect import load, save
from editor import DATE_ZONE
from model_cost import configured_price, estimate, worst_case
from release import ReleaseMarkerMismatch

CODE = Path(__file__).resolve().parent.parent
ROOT = Path(os.getenv('VENTURE_DATA', '/data')).resolve()
DB = ROOT / 'venture.sqlite'
PRIVATE = Path(os.environ.get('VENTURE_PRIVATE', ROOT / 'private'))
REPO = PRIVATE / 'site'
STATE = REPO / '.venture-runtime'
ITEMS = PRIVATE / 'items.json'
JOURNAL = PRIVATE / 'publish.json'
BACKUPS = PRIVATE / 'backups'
REMOTE = 'https://github.com/yabby-groups/codex-venture.git'
STOP = threading.Event()
DEPLOY_WAIT_SECONDS = 480
DEPLOY_RECHECK_SECONDS = 60
INTERVALS = {'collect': 15, 'discover': 30, 'news': 30, 'resource-discover': 30,
             'resource-sync': 30, 'practices': 120, 'stories': 120,
             'resource-refresh': 360, 'backfill': 1440}
PRIORITIES = {'collect': 25, 'news': 25, 'backfill': 1, 'resource-refresh': 5}
PHASES = {'scheduler': {'backup'}, 'collector': set(INTERVALS) | {'daily', 'weekly', 'analytics-daily'},
          'editor': {'edit'}, 'publisher': {'publish', 'verify'}}
CONTENT = ('src/content/news', 'src/content/daily', 'src/content/resources')


@contextmanager
def lock(name, nonblocking=False):
    with (ROOT / (name + '.lock')).open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX | (fcntl.LOCK_NB if nonblocking else 0))
        yield


def git(*args, write=False, capture=False):
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
    command = ['git', '-C', str(REPO), *args]
    if write:
        env['VENTURE_GIT_TOKEN'] = secret('github_write')
        command = [str(CODE / 'ops/hosted-git'), *command]
    result = subprocess.run(command, check=True, env=env, text=True, timeout=90,
                            stdout=subprocess.PIPE if capture else None)
    return result.stdout.strip() if capture else None


def secret(name, optional=False):
    path = Path('/run/secrets') / name
    if optional and not path.exists():
        return ''
    value = path.read_text().strip()
    if not value and not optional:
        raise ValueError(f'Empty secret {name}')
    return value


def checkout():
    REPO.mkdir(parents=True, exist_ok=True)
    if not (REPO / '.git').exists():
        git('init')
        git('remote', 'add', 'origin', REMOTE)
    git('fetch', '--no-tags', 'origin', 'refs/heads/main:refs/remotes/origin/main')
    git('checkout', '--detach', '--force', 'origin/main')
    if not ITEMS.exists():
        shutil.copyfile(REPO / 'state/items.json', ITEMS)
    else:
        shutil.copyfile(ITEMS, REPO / 'state/items.json')
    git('clean', '-fd', '--', *CONTENT)
    lockfile = (CODE / 'package-lock.json').read_text()
    if (REPO / 'package-lock.json').read_text() != lockfile:
        raise RuntimeError('Rebuild operator image for the current package-lock.json')
    fingerprint = hashlib.sha256(lockfile.encode()).hexdigest()
    dependencies = REPO / 'node_modules'
    stamp = dependencies / '.venture-lock'
    if not stamp.is_file() or stamp.read_text() != fingerprint:
        temporary = REPO / '.venture-runtime' / 'dependencies'
        shutil.rmtree(temporary, ignore_errors=True)
        temporary.parent.mkdir(exist_ok=True)
        shutil.copytree(CODE / 'node_modules', temporary, symlinks=True)
        (temporary / stamp.name).write_text(fingerprint)
        shutil.rmtree(dependencies, ignore_errors=True)
        temporary.rename(dependencies)


def dispatch(db, kind, key):
    priority = PRIORITIES.get(kind, 15)
    queue.enqueue(db, 'collector', kind, key, priority=priority)


def live(db, kind):
    return db.execute("""
        SELECT 1 FROM tasks WHERE status IN ('pending','running','retry')
        AND (type=? OR json_extract(payload,'$.kind')=?) LIMIT 1
    """, (kind, kind)).fetchone()


def schedule(db):
    now = datetime.now(DATE_ZONE)
    with queue.transaction(db):
        queue.recover(db, time.time())
        if queue.setting(db, 'paused', True):
            return
        for kind, minutes in INTERVALS.items():
            interval = int(os.getenv('VENTURE_' + kind.upper().replace('-', '_') + '_MINUTES', minutes))
            if interval < 1:
                raise ValueError(f'Invalid interval for {kind}')
            if kind == 'backfill' and (live(db, 'collect') or live(db, 'news')):
                continue
            if not live(db, kind):
                dispatch(db, kind, f'{kind}:{int(now.timestamp()) // (interval * 60)}')
        if now.hour >= 12:
            dispatch(db, 'analytics-daily', f'analytics-daily:{now.date()}')
        if now.hour >= 20:
            dispatch(db, 'daily', f'daily:{now.date()}')
            if now.weekday() == 6:
                dispatch(db, 'weekly', f'weekly:{now.date()}')
        queue.enqueue(db, 'scheduler', 'backup', f'backup:{now.date()}')
        db.execute("""
            UPDATE tasks SET payload='{}'
            WHERE status='completed' AND type IN ('edit','publish') AND payload!='{}' AND finished_at<?
        """, (time.time() - 7 * 86400,))


def configure_phase(path):
    import hosted
    hosted.WORK = path
    hosted.BATCH = path / 'batch.json'
    hosted.MODEL = path / 'model'
    hosted.REPOSITORY = CODE
    return hosted


def pending_publication():
    journal = load(JOURNAL, {})
    if not journal:
        return {}
    with queue.connect(DB) as db:
        row = db.execute('SELECT status FROM tasks WHERE id=?', (journal['task'],)).fetchone()
    if row and row['status'] == 'completed':
        JOURNAL.unlink(missing_ok=True)
        return {}
    return journal


def prepare(kind):
    token = secret('github_read', optional=True)
    if token:
        os.environ['VENTURE_GITHUB_READ_TOKEN'] = token
    os.environ['VENTURE_COLLECTION_LANE'] = 'resource' if kind.startswith('resource-') or kind == 'backfill' else 'news'
    with lock('state'), tempfile.TemporaryDirectory(prefix='venture-collect-') as temp:
        if pending_publication():
            raise RuntimeError('Publication recovery must finish before changing operating state')
        checkout()
        os.chdir(REPO)
        os.environ['RUNNER_TEMP'] = temp
        path = Path(temp) / 'venture'
        hosted = configure_phase(path)
        with queue.connect(DB) as db:
            active = db.execute("""
                SELECT payload FROM tasks WHERE type IN ('edit','publish')
                AND status IN ('pending','running','retry','blocked')
                AND json_extract(payload,'$.kind')=?
            """, (kind,)).fetchall()
        excluded = {key for row in active for batch in json.loads(row[0])['batch']['batches']
                    for key in batch['candidates']}
        hosted.prepare(kind, queued=True, excluded=excluded)
        save(ITEMS, load(REPO / 'state/items.json', {}))
        inventory = json.loads(subprocess.check_output(['node', 'scripts/metadata.mjs'], text=True))
        today = datetime.now(DATE_ZONE).date().isoformat()
        counts = {}
        for article in inventory:
            kind_name = article.get('type') or article['collection']
            row = counts.setdefault(kind_name, {'total': 0, 'today': 0})
            row['total'] += 1
            row['today'] += str(article['published']).startswith(today)
        resource_counts = {}
        for file in (REPO / 'src/content/resources').glob('*.json'):
            rows = load(file, [])
            if isinstance(rows, list):
                resource_counts[file.stem] = len(rows)
        return {'inventory': {'articles': counts, 'resources': resource_counts}, 'batch': load(hosted.BATCH, None), 'collection': load(path / 'collection.json', {})}


def run_editor(payload):
    os.environ['CODEX_API_KEY'] = secret('codex_api_key')
    batch = dict(payload['batch'],
                 unlimited=os.getenv('VENTURE_DAILY_TOKEN_LIMIT') == 'unlimited',
                 enforce_cost_limit=bool(os.getenv('VENTURE_DAILY_COST_LIMIT')))
    with tempfile.TemporaryDirectory(prefix='venture-model-') as temp:
        hosted = configure_phase(Path(temp))
        save(hosted.BATCH, batch)
        try:
            hosted.invoke(yolo=True)
        except (OSError, ValueError, RuntimeError) as error:
            return {'error': str(error), 'receipt': load(hosted.MODEL / 'receipt.json', {})}
        return {'response': load(hosted.MODEL / 'response.json', []),
                'receipt': load(hosted.MODEL / 'receipt.json', {})}


def build(path):
    subprocess.run(['npm', 'run', 'build'], check=True, timeout=300)
    if load(path / 'routes.json', []):
        subprocess.run(['node', str(CODE / 'scripts/check-articles-browser.mjs'),
                        str(path / 'routes.json')], check=True, timeout=120)


def apply_published(journal):
    # Idempotent replay until the journal is removed.
    save(ITEMS, journal['items'])
    if journal['resources'] is not None:
        save(STATE / 'resources.json', journal['resources'])


def publish(task, payload):
    import re

    journal_path = JOURNAL
    with lock('state'), tempfile.TemporaryDirectory(prefix='venture-publish-') as temp:
        checkout()
        os.chdir(REPO)
        path = Path(temp)
        hosted = configure_phase(path)
        journal = pending_publication()
        if journal and journal['task'] != task:
            raise RuntimeError(f'Publication recovery belongs to task {journal["task"]}')
        if journal:
            pushed = subprocess.run(['git', 'merge-base', '--is-ancestor', journal['sha'], 'origin/main'],
                                    timeout=30).returncode
            if pushed == 0:
                apply_published(journal)
                return journal['verification']
            if pushed != 1:
                raise RuntimeError('Cannot determine prior Git push result')
            journal_path.unlink()

        batch = payload['batch']
        # Acceptance mutates state during validation. Redirect state mutations to staging files.
        shutil.copyfile(ITEMS, path / 'items.json') if ITEMS.exists() else save(path / 'items.json', {})
        if (STATE / 'resources.json').exists():
            shutil.copyfile(STATE / 'resources.json', path / 'resources.json')
        hosted.ITEMS = path / 'items.json'
        hosted.resource_ingest.STATE = path / 'resources.json'
        save(hosted.BATCH, batch)
        save(path / 'result/response.json', payload['response'])
        hosted.accept()
        items = load(hosted.ITEMS, {})
        resources = load(hosted.resource_ingest.STATE, None)
        git('add', '--', *CONTENT)
        changes = git('diff', '--cached', '--name-status', capture=True)
        journal = dict(task=task, items=items, resources=resources)
        if not changes:
            apply_published(journal)
            return {'published': False}
        allowed = r'(?:A\tsrc/content/(?:news|daily)|M\tsrc/content/news)/[a-z0-9]+(?:-[a-z0-9]+)*\.md|[AM]\tsrc/content/resources/[a-z0-9]+(?:-[a-z0-9]+)*\.json'
        if any(not re.fullmatch(allowed, row) for row in changes.splitlines()):
            raise ValueError('Unexpected publication path or operation')
        build(path)
        if os.getenv('VENTURE_MODE', 'validation') != 'production':
            return {'published': False, 'validated': True, 'changes': changes.splitlines()}
        git('-c', 'user.name=Codex Venture', '-c', 'user.email=codex-venture@users.noreply.github.com',
            'commit', '-m', 'Publish Codex Venture bilingual coverage')
        sha = git('rev-parse', 'HEAD', capture=True)
        verification = dict(published=True, sha=sha, routes=load(path / 'routes.json', []),
                            resource_routes=load(path / 'resource-routes.json', []))
        git('update-ref', 'refs/venture/publication', sha)
        save(journal_path, {**journal, 'sha': sha, 'verification': verification})
        git('push', 'origin', 'HEAD:refs/heads/main', write=True)
        apply_published(journal)
        return verification


def verify(payload):
    with lock('state', nonblocking=True), tempfile.TemporaryDirectory(prefix='venture-verify-') as temp:
        checkout()
        os.chdir(REPO)
        path = Path(temp)
        hosted = configure_phase(path)
        current = git('rev-parse', 'HEAD', capture=True)
        git('merge-base', '--is-ancestor', payload['sha'], current)
        save(path / 'routes.json', payload['routes'])
        save(path / 'resource-routes.json', payload['resource_routes'])
        build(path)
        try:
            hosted.health()
        except ReleaseMarkerMismatch as error:
            return {'deployment_pending': str(error)}
        return {'sha': current, 'publication_sha': payload['sha'],
                'release': Path('dist/release.txt').read_text().strip(), 'verified': True,
                'coverage': load(Path('dist/coverage.json'), {})}


def backup():
    BACKUPS.mkdir(exist_ok=True)
    with lock('state'):
        with tempfile.TemporaryDirectory(prefix='.backup-', dir=BACKUPS) as temp:
            directory = Path(temp)
            with queue.connect(DB) as source, sqlite3.connect(directory / DB.name) as target:
                source.backup(target)
                if target.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
                    raise RuntimeError('Backup integrity check failed')
            if STATE.exists():
                shutil.copytree(STATE, directory / 'runtime', ignore=shutil.ignore_patterns('site'))
            if ITEMS.exists():
                shutil.copyfile(ITEMS, directory / 'items.json')
            if JOURNAL.exists():
                shutil.copyfile(JOURNAL, directory / 'publish.json')
                # Keep the pre-push commit reachable after restoring the journal.
                git('bundle', 'create', str(directory / 'publication.bundle'), 'refs/venture/publication')
            destination = BACKUPS / datetime.now(DATE_ZONE).strftime('%Y%m%dT%H%M%S%f')
            directory.rename(destination)
    for expired in sorted(p for p in BACKUPS.iterdir() if p.name[0].isdigit())[:-14]:
        shutil.rmtree(expired)
    return {'backup': destination.name}


def phase(task, kind, payload):
    if kind == 'edit':
        return run_editor(payload)
    if kind == 'publish':
        return publish(task, payload)
    if kind == 'verify':
        return verify(payload)
    if kind == 'backup':
        return backup()
    if kind == 'analytics-daily':
        from analytics import operator_daily
        from editor import metadata
        with lock('state'):
            checkout()
            articles = metadata(REPO)
        return operator_daily(PRIVATE / 'analytics', articles)
    return prepare(kind)


def reserve(db, task, payload):
    batch = payload['batch']
    day = datetime.now(DATE_ZONE).date().isoformat()
    limit = os.getenv('VENTURE_DAILY_TOKEN_LIMIT') or '100000'
    cost_limit = os.getenv('VENTURE_DAILY_COST_LIMIT')
    model = (os.getenv('CODEX_ADVANCED_MODEL') if batch['task'] == 'weekly' else None) or os.getenv('CODEX_MODEL')
    price = configured_price('venture', model, day)
    compatible = price and price['cache_in_input'] and price['reasoning_in_output']
    if cost_limit and (not compatible or price['currency'] != os.getenv('VENTURE_COST_CURRENCY')):
        return False
    cost = worst_case(price, batch['reservation']) if compatible else None
    return queue.reserve(db, task, day, batch['reservation'], cost,
                         None if limit == 'unlimited' else int(limit),
                         Decimal(cost_limit) if cost_limit else None,
                         Decimal(queue.setting(db, 'legacy_cost', {}).get(day))
                         if day in queue.setting(db, 'legacy_cost', {}) else None)


def settle(db, task, receipt):
    if not receipt.get('batches'):
        return False
    row = receipt['batches'][0]
    if row['sessions'] == 0:
        db.execute('DELETE FROM model_usage WHERE task=?', (task,))
        return True
    if row['usage'] is None:
        db.execute('UPDATE model_usage SET receipt=? WHERE task=?', (json.dumps(receipt), task))
        return False
    day = db.execute('SELECT day FROM model_usage WHERE task=?', (task,)).fetchone()[0]
    price = configured_price('venture', row.get('model'), day)
    priced = estimate(row['usage'], price)
    tokens = row['usage']['input_tokens'] + row['usage']['output_tokens']
    db.execute("""
        UPDATE model_usage SET tokens=?,cost=COALESCE(?,cost),receipt=? WHERE task=?
    """, (tokens, priced['amount'] if priced else None, json.dumps(receipt), task))
    return True


def complete(db, row, owner, payload, result):
    task, kind = row['id'], row['type']
    if kind == 'publish' and result.get('published'):
        queue.store(db, 'last_push', result)
    if 'inventory' in result:
        queue.store(db, 'inventory', result['inventory'])
    if 'coverage' in result:
        queue.store(db, 'coverage', result['coverage'])
    if kind == 'verify':
        queue.store(db, 'production', {**result, 'verified_at': time.time()})
        queue.store(db, 'published:' + payload['kind'], time.time())
    if kind == 'edit':
        known = settle(db, task, result.get('receipt', {}))
        if 'error' in result:
            queue.finish(db, task, owner, 'dead' if known else 'blocked', result,
                         error=result['error'])
            return
        if payload['kind'] != 'model-probe':
            queue.enqueue(db, 'publisher', 'publish', f'publish:{task}',
                          {**payload, 'response': result['response']}, row['priority'])
    elif kind == 'publish' and result.get('published'):
        queue.enqueue(db, 'publisher', 'verify', f'verify:{task}',
                      {**result, 'kind': payload['kind']}, 30, delay=20)
    elif result.get('batch') and os.getenv('VENTURE_MODE', 'validation') == 'production':
        queue.enqueue(db, 'editor', 'edit', f'edit:{task}',
                      {'batch': result['batch'], 'kind': kind}, row['priority'])
    elif kind in ('collect', 'discover') and not live(db, 'news'):
        dispatch(db, 'news', f'news:collect:{task}')
    public_result = {key: value for key, value in result.items() if key not in ('batch', 'response')}
    queue.finish(db, task, owner, 'completed', public_result)


def execute(row, owner):
    task, kind = row['id'], row['type']
    payload = json.loads(row['payload'])
    with queue.connect(DB) as db, tempfile.TemporaryDirectory(prefix='venture-phase-') as temp:
        path = Path(temp)
        save(path / 'payload.json', payload)
        if kind == 'edit':
            if os.getenv('VENTURE_MODE', 'validation') != 'production' and payload['kind'] != 'model-probe':
                queue.finish(db, task, owner, 'retry', error='Model calls disabled in validation mode', delay=900)
                return
            with queue.transaction(db):
                if not reserve(db, task, payload):
                    queue.finish(db, task, owner, 'retry', error='Model budget or pricing unavailable', delay=900)
                    return
        process = subprocess.Popen([sys.executable, __file__, '_phase', str(task), kind, str(path)],
                                   cwd=CODE, start_new_session=True)
        try:
            deadline = time.monotonic() + 1000
            while process.poll() is None:
                if STOP.wait(5) or time.monotonic() >= deadline or not queue.renew(db, task, owner):
                    raise RuntimeError('Worker shutdown, timeout or lease loss')
            if process.returncode:
                raise RuntimeError(f'{kind} phase exit {process.returncode}')
            result = load(path / 'result.json', None)
            if kind == 'verify' and result and result.get('deployment_pending'):
                remaining = row['created_at'] + DEPLOY_WAIT_SECONDS - time.time()
                if remaining <= 0:
                    raise RuntimeError(f"Cloudflare deployment not verified within "
                                       f"{DEPLOY_WAIT_SECONDS} seconds: {result['deployment_pending']}")
                print(f'Task {task} (verify): waiting for Cloudflare deployment', flush=True)
                queue.finish(db, task, owner, 'retry', delay=min(DEPLOY_RECHECK_SECONDS, remaining))
                return
            with queue.transaction(db):
                complete(db, row, owner, payload, result)
            if kind == 'publish':
                with lock('state'):
                    journal = load(JOURNAL, {})
                    if journal.get('task') == task:
                        JOURNAL.unlink()
        except Exception as error:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=8)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
            print(f'Task {task} ({kind}): {error}', flush=True)
            count = row['attempts'] + 1
            journal = load(JOURNAL, {}) if kind == 'publish' else {}
            durable = kind == 'verify' or journal.get('task') == task
            status = 'blocked' if kind == 'edit' else 'dead' if count >= 5 and not durable else 'retry'
            queue.finish(db, task, owner, status, error=str(error), delay=min(900, 15 * 2 ** min(count, 6)))


def serve(role):
    signal.signal(signal.SIGTERM, lambda *_: STOP.set())
    signal.signal(signal.SIGINT, lambda *_: STOP.set())
    workers = int(os.getenv('VENTURE_EDITOR_CONCURRENCY', '2')) if role == 'editor' else 1
    if role not in PHASES:
        raise ValueError(f'Unknown service role {role}')
    if not 1 <= workers <= 2:
        raise ValueError('Editor concurrency must be 1 or 2')
    initialize()
    owner = f'{role}:{os.getpid()}:{time.time_ns()}'
    with lock(role, nonblocking=True), queue.connect(DB) as db, ThreadPoolExecutor(workers) as pool:
        active = set()
        tick = 0
        while not STOP.is_set():
            for future in tuple(active):
                if future.done():
                    active.remove(future)
                    future.result()
            now = time.time()
            db.execute('INSERT OR REPLACE INTO heartbeat VALUES (?,?)', (role, now))
            if role == 'scheduler' and now >= tick:
                schedule(db)
                tick = now + 60
            while len(active) < workers and (row := queue.claim(db, role, owner)):
                active.add(pool.submit(execute, row, owner))
            STOP.wait(2)


def initialize():
    ROOT.mkdir(parents=True, exist_ok=True)
    queue.initialize(DB)


def main():
    parser = argparse.ArgumentParser(prog='venture')
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('init', 'status', 'queue', 'sources', 'report', 'budget', 'pause', 'resume', 'backup', 'doctor', 'export-hosted'):
        commands.add_parser(name)
    for name, argument in (('serve', 'role'), ('health', 'role'), ('run', 'kind'),
                           ('retry', 'task'), ('import-state', 'ref'), ('restore', 'backup')):
        commands.add_parser(name).add_argument(argument)
    legacy = commands.add_parser('legacy-cost')
    legacy.add_argument('day')
    legacy.add_argument('amount')
    args = parser.parse_args()
    initialize()
    if args.command == 'serve':
        serve(args.role)
        return
    with queue.connect(DB) as db:
        result = manage(args, db)
    if result is not None:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__' and sys.argv[1:2] == ['_phase']:
    _, _, task, kind, directory = sys.argv
    path = Path(directory)
    save(path / 'result.json', phase(int(task), kind, load(path / 'payload.json', {})))


@contextmanager
def offline():
    with lock('state'):
        with queue.connect(DB) as db:
            if not queue.setting(db, 'paused', True):
                raise RuntimeError('Pause operations before changing durable state')
            queue.recover(db, time.time())
            if db.execute("SELECT 1 FROM tasks WHERE status='running' AND type!='backup' LIMIT 1").fetchone():
                raise RuntimeError('Wait for running tasks to drain')
        yield


def import_state(ref):
    with offline():
        checkout()
        git('fetch', '--no-tags', 'origin', 'refs/heads/venture-state:refs/remotes/origin/venture-state')
        sha = git('rev-parse', ref, capture=True)
        with queue.connect(DB) as db:
            if queue.setting(db, 'imported') == sha:
                return {'imported': sha, 'already_imported': True}
            if queue.setting(db, 'imported') or db.execute('SELECT 1 FROM model_usage LIMIT 1').fetchone():
                raise RuntimeError('Import final Hosted state into a fresh, paused data volume')
        BACKUPS.mkdir(exist_ok=True)
        archive = BACKUPS / f'hosted-{sha}.tar'
        git('archive', '--format=tar', '-o', str(archive), sha)
        files = {}
        for record in git('ls-tree', '-r', sha, capture=True).splitlines():
            info, name = record.split('\t')
            mode, object_type, blob = info.split()
            if mode != '100644' or object_type != 'blob':
                raise ValueError(f'Unsupported imported entry {name}')
            raw = git('cat-file', 'blob', blob, capture=True)
            files[name] = json.loads(raw)
        mandatory = {'state/items.json', '.venture-runtime/usage.json'}
        if not mandatory.issubset(files):
            raise ValueError('Missing items or usage ledger in source branch')
        for name, value in files.items():
            if name == 'state/items.json':
                save(ITEMS, value)
            elif Path(name).parent == Path('.venture-runtime') and name.endswith('.json'):
                save(REPO / name, value)
        with queue.connect(DB) as db, queue.transaction(db):
            for day, value in files['.venture-runtime/usage.json'].items():
                db.execute('INSERT OR REPLACE INTO legacy_usage VALUES (?,?)', (day, json.dumps(value)))
            queue.store(db, 'imported', sha)
        return {'imported': sha, 'files': sorted(files), 'archive': archive.name}


def restore(name):
    if not name.isdigit() and not (name.replace('T', '', 1).isdigit() and name.count('T') == 1):
        raise ValueError('Expected a backup directory name')
    with offline():
        directory = BACKUPS / name
        if not (directory / DB.name).is_file():
            raise ValueError('Backup database missing')
        with sqlite3.connect(directory / DB.name) as source, queue.connect(DB) as target:
            if source.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
                raise ValueError('Backup database failed integrity check')
            target.execute('ATTACH DATABASE ? AS restored', (str(directory / DB.name),))
            if target.execute("""
                SELECT 1 FROM model_usage m LEFT JOIN restored.model_usage r ON r.task=m.task
                WHERE r.task IS NULL OR r.tokens!=m.tokens OR r.cost IS NOT m.cost LIMIT 1
            """).fetchone():
                raise RuntimeError('Restore would drop or alter model usage')
            target.execute('DETACH DATABASE restored')
            source.backup(target)
            with queue.transaction(target):
                queue.recover(target, time.time() + queue.LEASE + 1)
                queue.store(target, 'paused', True)
        checkout()
        if (directory / 'publication.bundle').exists():
            git('fetch', str(directory / 'publication.bundle'),
                'refs/venture/publication:refs/venture/publication')
        if STATE.exists():
            shutil.rmtree(STATE)
        if (directory / 'runtime').exists():
            shutil.copytree(directory / 'runtime', STATE)
        for file, target in (('items.json', ITEMS), ('publish.json', JOURNAL)):
            if (directory / file).exists():
                save(target, load(directory / file, {}))
            else:
                target.unlink(missing_ok=True)
        return {'restored': name, 'paused': True}


def records(db, sql, values=()):
    return [dict(row) for row in db.execute(sql, values)]


def report(db):
    now = datetime.now(DATE_ZONE)
    production = queue.setting(db, 'production', {})
    last_push = queue.setting(db, 'last_push', {})
    return {
        'paused': queue.setting(db, 'paused', True),
        'services': records(db, 'SELECT * FROM heartbeat'),
        'tasks': records(db, 'SELECT role,type,status,count(*) AS count FROM tasks GROUP BY role,type,status'),
        'last_collection_success': records(db, """
            SELECT MAX(finished_at) AS timestamp FROM tasks WHERE status='completed'
            AND json_extract(result,'$.collection.succeeded')>0
        """)[0]['timestamp'],
        'publication': {kind: queue.setting(db, 'published:' + kind)
                        for kind in ('news', 'practices', 'stories', 'daily', 'weekly', 'resource-sync',
                                     'resource-refresh', 'backfill')},
        'production': production,
        'verification_pending': bool(last_push and last_push['sha'] != production.get('publication_sha')),
        'source_health': {key: {
            'success_rate': value.get('successes', 0) /
                (value.get('successes', 0) + value.get('failed_requests', 0))
                if value.get('successes', 0) + value.get('failed_requests', 0) else None,
            'last_success': value.get('last_success'), 'error': value.get('error'),
            'budget_pause': value.get('budget_pause'),
        } for key, value in load(STATE / 'health.json', {}).items()},
        'candidate_backlog': sum(value.get('status') == 'pending' for value in load(ITEMS, {}).values()),
        'resource_backlog': sum(not value.get('done') for value in
                                load(STATE / 'resources.json', {}).get('rows', {}).values()),
        'source_requests': load(STATE / 'requests.json', {}),
        'budget': budget(db),
        'content': queue.setting(db, 'inventory', {}),
        'verified_coverage': queue.setting(db, 'coverage', {}),
        'attention': ('No verified publication within 24 hours' if now.timestamp() -
                      production.get('verified_at', 0) > 86400 else None),
    }


def budget(db):
    day = datetime.now(DATE_ZONE).date().isoformat()
    return {'date': day, 'inherited': records(db, 'SELECT * FROM legacy_usage WHERE day=?', (day,)),
            'vps': records(db, 'SELECT * FROM model_usage WHERE day=?', (day,)),
            'token_limit': os.getenv('VENTURE_DAILY_TOKEN_LIMIT') or '100000',
            'cost_limit': os.getenv('VENTURE_DAILY_COST_LIMIT') or None,
            'currency': os.getenv('VENTURE_COST_CURRENCY') or None}


def manage(args, db):
    action = args.command
    if action == 'init':
        return {'database': str(DB), 'paused': queue.setting(db, 'paused', True)}
    if action == 'health':
        row = db.execute('SELECT updated_at FROM heartbeat WHERE role=?', (args.role,)).fetchone()
        raise SystemExit(0 if row and time.time() - row[0] < 45 else 1)
    if action in ('status', 'report'):
        return report(db)
    if action == 'queue':
        return records(db, """
            SELECT id,type,role,status,attempts,available_at,last_error
            FROM tasks ORDER BY id DESC LIMIT 200
        """)
    if action == 'sources':
        return load(STATE / 'health.json', {})
    if action == 'budget':
        return budget(db)
    if action in ('pause', 'resume'):
        with queue.transaction(db):
            paused = action == 'pause'
            if not paused and os.getenv('VENTURE_MODE', 'validation') == 'production':
                if not queue.setting(db, 'imported') or os.getenv('VENTURE_HOSTED_DRAINED') != 'true':
                    raise RuntimeError('Import final Hosted state after draining Hosted jobs')
            queue.store(db, 'paused', paused)
        return {'paused': paused}
    if action == 'run':
        if args.kind == 'model-probe':
            if os.getenv('VENTURE_MODE', 'validation') != 'validation':
                raise ValueError('Run the model probe in validation mode')
            day = datetime.now(DATE_ZONE).date().isoformat()
            batch = dict(task='news', date=day, existingResources=[], reservation=int(os.getenv('VENTURE_RUN_TOKENS', '25000')),
                         unlimited=False, enforce_cost_limit=bool(os.getenv('VENTURE_DAILY_COST_LIMIT')),
                         batches=[{'candidates': {}}])
            with queue.transaction(db):
                if not queue.setting(db, 'imported'):
                    raise RuntimeError('Import Hosted usage before running a model probe')
                queue.enqueue(db, 'editor', 'edit', 'model-probe:editor-only:' + day,
                              {'kind': 'model-probe', 'batch': batch}, 30)
            return {'enqueued': args.kind}
        if args.kind not in PHASES['collector']:
            raise ValueError('Unknown collection or editorial task')
        dispatch(db, args.kind, f'manual:{args.kind}:{time.time_ns()}')
        return {'enqueued': args.kind}
    if action == 'retry':
        task = int(args.task)
        with queue.transaction(db):
            if db.execute('SELECT 1 FROM model_usage WHERE task=?', (task,)).fetchone():
                raise RuntimeError('Model usage exists. Retain the reservation and review the provider receipt.')
            db.execute("""UPDATE tasks SET status='retry',attempts=0,available_at=?,updated_at=?
                          WHERE id=? AND status IN ('blocked','dead','retry')""",
                       (time.time(), time.time(), task))
        return {'task': task}
    if action == 'backup':
        key = 'backup:manual:' + str(time.time_ns())
        queue.enqueue(db, 'scheduler', 'backup', key, priority=30)
        return {'enqueued': key}
    if action == 'import-state':
        return import_state(args.ref)
    if action == 'restore':
        return restore(args.backup)
    if action == 'legacy-cost':
        day = datetime.fromisoformat(args.day).date().isoformat()
        amount = Decimal(args.amount)
        if not amount.is_finite() or amount < 0:
            raise ValueError('Use a finite, nonnegative amount')
        with offline(), queue.transaction(db):
            costs = queue.setting(db, 'legacy_cost', {})
            costs[day] = str(amount)
            queue.store(db, 'legacy_cost', costs)
        return {'day': day, 'legacy_cost': str(amount)}
    if action == 'export-hosted':
        with offline():
            if pending_publication():
                raise RuntimeError('Complete pending publication recovery before export')
            BACKUPS.mkdir(exist_ok=True)
            directory = Path(tempfile.mkdtemp(prefix='hosted-export-', dir=BACKUPS))
            shutil.copytree(STATE, directory / '.venture-runtime', ignore=shutil.ignore_patterns('site'))
            save(directory / 'state/items.json', load(ITEMS, {}))
            ledger = {row['day']: json.loads(row['data']) for row in db.execute('SELECT * FROM legacy_usage')}
            for row in db.execute('SELECT day,SUM(tokens) AS tokens,COUNT(*) AS calls FROM model_usage GROUP BY day'):
                day = ledger.setdefault(row['day'], {'tokens': 0, 'calls': 0})
                for field in ('tokens', 'calls'):
                    day[field] += row[field]
            save(directory / '.venture-runtime/usage.json', ledger)
        return {'directory': str(directory)}
    if action == 'doctor':
        return {'integrity': db.execute('PRAGMA quick_check').fetchone()[0],
                'disk_free_bytes': shutil.disk_usage(ROOT).free,
                'mode': os.getenv('VENTURE_MODE', 'validation'), 'status': report(db)}
    raise ValueError(f'Unknown command {action}')


if __name__ == '__main__' and sys.argv[1:2] != ['_phase']:
    main()
