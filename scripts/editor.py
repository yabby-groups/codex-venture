import json
import os
import re
import signal
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from collect import canonical, digest, load, save, timestamp
from release import RUNTIME

ITEMS = Path('state/items.json')
DATE_ZONE = ZoneInfo('Asia/Shanghai')
CANDIDATE_LIMIT = 8
DAILY_BUDGET = int(os.environ.get('VENTURE_DAILY_TOKENS', '100000'))
RUN_BUDGET = int(os.environ.get('VENTURE_RUN_TOKENS', '25000'))


def output_schema():
    string = {'type': 'string'}
    strings = {'type': 'array', 'items': string}
    fields = {key: string for key in ('slug', 'titleZh', 'titleEn', 'summaryZh', 'summaryEn', 'category', 'body')}
    fields.update(tags=strings, itemIds=strings)

    def obj(properties):
        return dict(type='object', properties=properties, required=list(properties), additionalProperties=False)

    return obj(dict(articles=dict(type='array', items=obj(fields)), skipped=strings))


def metadata():
    return json.loads(subprocess.check_output(['node', 'scripts/metadata.mjs'], text=True))


def sync(items, articles):
    for story in articles:
        for source in story['sources']:
            entry = items.get(digest(canonical(source['url'])))
            if entry:
                article = f"/{story['collection']}/{story['slug']}/"
                entry.update(status='published', articles=sorted(set(entry.get('articles', [])) | {article}))


def budget_path(day):
    return RUNTIME / f'tokens-{day}.json'


def event_usage(text):
    for line in text.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get('type') == 'turn.completed':
            usage = event.get('usage', {})
            return usage.get('input_tokens', 0) + usage.get('output_tokens', 0)
    return None


def invoke(prompt, day):
    budget_file = budget_path(day)
    spent = load(budget_file, {'tokens': 0})['tokens']
    if spent + RUN_BUDGET > DAILY_BUDGET:
        print('Daily Codex token budget exhausted')
        return None
    save(budget_file, {'tokens': spent + RUN_BUDGET})
    schema, result = RUNTIME / 'editor-schema.json', RUNTIME / 'editor-result.json'
    save(schema, output_schema())
    result.unlink(missing_ok=True)
    command = [
        os.environ.get('VENTURE_CODEX', 'codex'), 'exec', '--ignore-user-config',
        '--ephemeral', '--json', '--sandbox', 'read-only',
        '-c', 'approval_policy="never"', '-c', 'model_reasoning_effort="low"',
        '--output-schema', str(schema), '-o', str(result), '-',
    ]
    if model := os.environ.get('VENTURE_MODEL'):
        command[2:2] = ['--model', model]
    with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True,
                          start_new_session=True) as process:
        try:
            events, _ = process.communicate(prompt, timeout=240)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.communicate()
            raise
    usage = event_usage(events)
    if usage is not None:
        save(budget_file, {'tokens': spent + usage})
        print(f'Codex used {usage} tokens')
    if process.returncode or not result.exists() or usage is None:
        raise RuntimeError(f'Codex failed or did not report usage ({process.returncode})')
    if usage > RUN_BUDGET:
        raise RuntimeError('Codex exceeded the per-run token budget')
    return load(result, {})


def choose(mode, items, now):
    day = now.date().isoformat()
    candidates = {}
    for key, item in sorted(items.items(), key=lambda pair: pair[1]['published'], reverse=True):
        if timestamp(item['published']) < now - timedelta(hours=48):
            continue
        eligible = item['status'] == 'pending'
        if mode == 'daily':
            eligible = eligible or any(path.startswith('/news/') for path in item.get('articles', []))
            eligible = eligible and not any(path.startswith('/daily/') for path in item.get('articles', []))
        if eligible and item.get('summary'):
            candidates[key] = {field: item[field] for field in ('title', 'url', 'published', 'summary', 'category')}
        if len(candidates) == CANDIDATE_LIMIT:
            break
    return candidates


def write_articles(response, mode, candidates, now):
    day = now.date().isoformat()
    writes = {}
    if len(response['articles']) > (1 if mode == 'daily' else 3):
        raise ValueError('too many articles')
    used = set()
    for article in response['articles']:
        slug, ids, body = [article.pop(key) for key in ('slug', 'itemIds', 'body')]
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug) or len(slug) > 100:
            raise ValueError('invalid article slug')
        if mode == 'daily' and slug != day:
            raise ValueError('invalid briefing date')
        if not ids or len(set(ids)) != len(ids) or used.intersection(ids):
            raise ValueError('missing or duplicated evidence')
        used.update(ids)
        evidence = [candidates[key] for key in ids]
        links = set(re.findall(r'href="([^"]+)"', body))
        valid_links = {item['url'] for item in evidence}
        if not links <= valid_links or (mode == 'daily' and links != valid_links):
            raise ValueError('article links do not match its evidence')
        if len(body) > 12000:
            raise ValueError('article too long')
        path = Path('src/content') / mode / (slug + '.md')
        if path.exists() or path in writes:
            raise ValueError(f'article already exists: {slug}')
        article['published'] = now.isoformat(timespec='seconds')
        article['sources'] = [dict(title=item['title'], url=item['url']) for item in evidence]
        # JSON scalar values are valid in YAML frontmatter.
        front = '\n'.join(f'{key}: {json.dumps(value, ensure_ascii=False)}' for key, value in article.items())
        writes[path] = f'---\n{front}\n---\n{body.strip()}\n'
    skipped = set(response['skipped'])
    if not skipped <= candidates.keys() or skipped & used:
        raise ValueError('invalid skipped candidate IDs')
    created = []
    try:
        for path, markdown in writes.items():
            with path.open('x') as handle:
                created.append(path)
                handle.write(markdown)
        metadata()
    except BaseException:
        for path in created:
            path.unlink(missing_ok=True)
        raise
    return skipped


def edit(mode):
    items = load(ITEMS, {})
    articles = metadata()
    sync(items, articles)
    now = datetime.now(DATE_ZONE)
    day = now.date().isoformat()
    for entry in items.values():
        if entry['status'] == 'pending' and timestamp(entry['published']) < now - timedelta(hours=48):
            entry['status'] = 'expired'
    save(ITEMS, items)
    if mode == 'daily' and any(story['collection'] == 'daily' and story['slug'] == day for story in articles):
        print('Daily briefing already exists')
        return
    candidates = choose(mode, items, now)
    if not candidates:
        print('No new candidates for the editorial window')
        return
    payload = json.dumps(dict(mode=mode, date=day, candidates=candidates), ensure_ascii=False)
    response = invoke(Path('ops/editor.md').read_text() + '\n\n' + payload, day)
    if response is None:
        return
    skipped = write_articles(response, mode, candidates, now)
    sync(items, metadata())
    for key in skipped:
        if items[key]['status'] == 'pending':
            items[key]['status'] = 'skipped'
    save(ITEMS, items)
