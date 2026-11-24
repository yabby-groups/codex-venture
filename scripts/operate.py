import argparse
import fcntl
import json
import os
import re
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from collect import collect, fetch, load, save, timestamp
from editor import ITEMS, edit, metadata, sync
from release import RUNTIME, commit, point, probe, recover, release


def maintenance():
    health = load(RUNTIME / 'health.json', {})
    items = load(ITEMS, {})
    now = datetime.now(timezone.utc)
    print(json.dumps({key: dict(failures=status.get('failures', 0), error=status.get('error'),
                               published=sum(item['source'] == key and item['status'] == 'published'
                                             for item in items.values()))
                      for key, status in sorted(health.items())}, ensure_ascii=False))
    config = Path('config/sources.yaml')
    text = config.read_text()
    changed = False
    # Discover maintained AI repos through GitHub's topic index. Admit at most one per week.
    query = 'https://api.github.com/search/repositories?q=topic%3Allm+stars%3A%3E3000+archived%3Afalse&sort=updated&per_page=10'
    try:
        body, _ = fetch(query, {})
        for candidate in json.loads(body)['items']:
            repo = candidate['full_name']
            if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo) or f'repo: {repo},' in text:
                continue
            key = 'github-' + repo.lower().replace('/', '-')
            body, _ = fetch(f'https://api.github.com/repos/{repo}/releases/latest', {})
            latest = json.loads(body)
            if not latest.get('body') or timestamp(latest['published_at']) < now - timedelta(days=30):
                continue
            text += f'  - {{id: {key}, kind: github, repo: {repo}, category: open-source}}\n'
            changed = True
            print(f'Added active open-source release feed {repo}')
            break
    except (ValueError, OSError, KeyError) as error:
        print(f'Source discovery deferred: {error}')
    # Retire only persistently failing sources after a week of observed failures.
    for key, status in sorted(health.items()):
        previous = status.get('last_success') or status.get('first_failure')
        if status.get('failures', 0) >= 8 and previous and timestamp(previous) < now - timedelta(days=7):
            pattern = rf'(^  - \{{id: {re.escape(key)}, [^\n}}]+)(\}})$'
            updated = re.sub(pattern, lambda m: m[0] if 'enabled:' in m[0] else m[1] + ', enabled: false}', text, flags=re.M)
            changed = changed or updated != text
            text = updated
    if changed:
        temporary = config.with_suffix('.tmp')
        temporary.write_text(text)
        temporary.replace(config)
    if os.environ.get('VENTURE_SITE_URL') and os.environ.get('VENTURE_DEPLOY_ROOT'):
        current = Path(os.environ['VENTURE_DEPLOY_ROOT']) / 'current'
        probe(os.environ['VENTURE_SITE_URL'], current.resolve().name)
    for path in RUNTIME.glob('tokens-*.json'):
        if path.stat().st_mtime < time.time() - 86400 * 30:
            path.unlink()


def pending_content():
    status = subprocess.check_output(['git', 'status', '--porcelain', '--', 'src/content'], text=True)
    return bool(status.strip())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('task', choices=('collect', 'sync', 'news', 'daily', 'weekly', 'deploy', 'rollback'))
    parser.add_argument('release_id', nargs='?')
    args = parser.parse_args()
    os.chdir(Path(__file__).resolve().parent.parent)
    RUNTIME.mkdir(exist_ok=True)
    with (RUNTIME / 'task.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('Another operation holds the task lock')
            return
        recover()
        if (RUNTIME / 'PAUSE').exists() and args.task != 'rollback':
            print('Operations paused')
            return
        if args.task in ('news', 'daily', 'weekly', 'deploy', 'collect'):
            if subprocess.check_output(['git', 'diff', '--cached', '--name-only'], text=True).strip():
                raise RuntimeError('finish the staged Git changes before running automation')
        if args.task == 'rollback':
            root = Path(os.environ['VENTURE_DEPLOY_ROOT']).resolve()
            key = args.release_id or ''
            if not re.fullmatch(r'[0-9a-f]{64}', key) or not (root / 'releases' / key / 'release.txt').is_file():
                parser.error('rollback requires a retained release ID')
            old = os.readlink(root / 'current') if (root / 'current').is_symlink() else None
            point(root, f'releases/{key}')
            try:
                probe(os.environ['VENTURE_SITE_URL'], key)
            except BaseException:
                point(root, old)
                raise
            return
        if args.task == 'sync':
            items = load(ITEMS, {})
            sync(items, metadata())
            save(ITEMS, items)
            return
        if args.task == 'deploy':
            release()
            return
        if args.task == 'weekly':
            maintenance()
        elif args.task == 'collect':
            collect()
            items = load(ITEMS, {})
            sync(items, metadata())
            save(ITEMS, items)
        else:
            if not pending_content():
                edit(args.task)
        if args.task in ('news', 'daily') and pending_content():
            release()
        elif not pending_content():
            commit()


if __name__ == '__main__':
    main()
