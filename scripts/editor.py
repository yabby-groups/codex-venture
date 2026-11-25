import json
import os
import re
import signal
from html import unescape
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from article_schema import BLOCKS, conforms
from collect import canonical, digest, load, save, timestamp
from release import RUNTIME
from resource_editor import PROFILES, UPDATES, resource_context, resource_profile, update_frontmatter

ITEMS = Path('state/items.json')
DATE_ZONE = ZoneInfo('Asia/Shanghai')
CANDIDATE_LIMIT = 8
CONTENT_TYPES = load(Path('config/content-types.json'), {})
DAILY_BUDGET = int(os.environ.get('VENTURE_DAILY_TOKENS', '100000'))
RUN_BUDGET = int(os.environ.get('VENTURE_RUN_TOKENS', '25000'))


def output_schema(candidates=None):
    string = {'type': 'string'}
    strings = {'type': 'array', 'items': string}
    candidate_ids = strings
    if candidates:
        candidate_ids = {**strings, 'items': {**string, 'enum': list(candidates)}}
    fields = {key: string for key in ('slug', 'titleZh', 'titleEn', 'summaryZh', 'summaryEn', 'category', 'body', 'type', 'version')}
    fields.update(tags=strings, itemIds=candidate_ids, blocks=BLOCKS, resource=PROFILES, resourceIds=strings)

    def obj(properties):
        return dict(type='object', properties=properties, required=list(properties), additionalProperties=False)

    update_fields = {**UPDATES['items']['properties'], 'itemIds': candidate_ids}
    updates = {**UPDATES, 'items': obj(update_fields)}
    return obj(dict(articles=dict(type='array', items=obj(fields)), skipped=candidate_ids, resourceUpdates=updates))


def metadata():
    return json.loads(subprocess.check_output(['node', 'scripts/metadata.mjs'], text=True))


def sync(items, articles):
    by_url = {item['url']: item for item in items.values()}
    for story in articles:
        for source in story['sources']:
            entry = by_url.get(canonical(source['url']))
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


def invoke(prompt, day, candidates):
    budget_file = budget_path(day)
    spent = load(budget_file, {'tokens': 0})['tokens']
    if spent + RUN_BUDGET > DAILY_BUDGET:
        print('Daily Codex token budget exhausted')
        return None
    save(budget_file, {'tokens': spent + RUN_BUDGET})
    schema, result = RUNTIME / 'editor-schema.json', RUNTIME / 'editor-result.json'
    save(schema, output_schema(candidates))
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


def choose(mode, items, now, days=2, strategy=None):
    strategy = strategy or {}
    limit = strategy.get('candidate_limit', CANDIDATE_LIMIT)
    weights = strategy.get('category_weights', {})
    candidates = {}
    groups = {}
    briefing = mode in ('daily', 'weekly')
    for key, item in items.items():
        content_type = item.get('content_type')
        source = item.get('source', '')
        details = item.get('discovery', {})
        group = content_type or ('release' if '/releases/' in item['url'] else
                                 'projects' if details.get('repository_id') else
                                 'research' if source.startswith(('arxiv-', 'hf-')) else 'news')
        if briefing and content_type:
            continue
        window = days if briefing else {'release': 14, 'projects': 30, 'research': 14, 'news': 7}.get(group)
        published = timestamp(item['published'])
        if window and published < now - timedelta(days=max(days, window)):
            continue
        eligible = item['status'] == 'pending' or (mode == 'backfill' and item['status'] == 'expired')
        if briefing:
            articles = item.get('articles', [])
            eligible = eligible or any(path.startswith('/news/') for path in articles)
            if mode == 'daily':
                eligible = eligible and not any(path.startswith('/daily/') for path in articles)
        if eligible and item.get('summary'):
            priority = (bool(item.get('evidence')), weights.get(item['category'], 0), published)
            groups.setdefault(group, []).append((priority, key))
    for group in groups.values():
        group.sort()
    byte_limit = 54000
    used_bytes = 0
    while groups and len(candidates) < limit:
        for group in sorted(groups, key=lambda name: groups[name][-1][0], reverse=True):
            _, key = groups[group].pop()
            if not groups[group]:
                del groups[group]
            item = items[key]
            evidence = {field: item[field] for field in ('title', 'url', 'published', 'summary', 'category')}
            evidence['summary'] = evidence['summary'][:1400]
            if item.get('content_type'):
                evidence['suggestedType'] = item['content_type']
            evidence['documents'] = item.get('evidence', [])[:3]
            evidence['lastVerified'] = item.get('verified_at')
            evidence['discovery'] = item.get('discovery', {})
            size = len(json.dumps(evidence, ensure_ascii=False).encode())
            if size + used_bytes <= byte_limit:
                candidates[key] = evidence
                used_bytes += size
            if len(candidates) == limit:
                break
    return candidates


def write_articles(response, mode, candidates, now, limit=3):
    day = now.date().isoformat()
    writes = {}
    revisions = {}
    articles = metadata()
    existing = [story["resource"] for story in articles if story.get("resource")]
    existing_ids = {row["id"] for row in existing}
    if mode in ('daily', 'weekly'):
        limit = min(limit, 1)
    if len(response['articles']) > limit:
        raise ValueError('too many articles')
    used = set()
    for article in response['articles']:
        profiles = article.pop('resource', [])
        related = article.pop('resourceIds', [])
        if not conforms(profiles, PROFILES) or len(profiles) > 1 or not set(related) <= existing_ids:
            raise ValueError('Invalid resource metadata or relation')
        blocks = article.pop('blocks', [])
        if not conforms(blocks, BLOCKS) or len(blocks) > 8:
            raise ValueError('invalid editorial blocks')
        if blocks:
            article['blocks'] = blocks
        slug, ids, body = [article.pop(key) for key in ('slug', 'itemIds', 'body')]
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug) or len(slug) > 100:
            raise ValueError('invalid article slug')
        if mode == 'weekly' and slug != 'weekly-' + day:
            raise ValueError('invalid weekly edition date')
        if mode == 'daily' and slug != day:
            raise ValueError('invalid briefing date')
        if not ids or len(set(ids)) != len(ids) or used.intersection(ids):
            raise ValueError('missing or duplicated evidence')
        if not set(ids) <= candidates.keys():
            raise ValueError(f'Unknown candidate IDs in article {slug}')
        used.update(ids)
        evidence = [candidates[key] for key in ids]
        links = set(map(unescape, re.findall(r'href="([^"]+)"', body)))
        valid_links = {item['url'] for item in evidence}
        primary_links = valid_links.copy()
        valid_links.update(doc['url'] for item in evidence for doc in item.get('documents', []))
        if not links <= valid_links or (mode in ('daily', 'weekly') and not primary_links <= links):
            raise ValueError('article links do not match its evidence')
        if len(body) > 12000:
            raise ValueError('article too long')
        collection = 'daily' if mode in ('daily', 'weekly') else 'news'
        path = Path('src/content') / collection / (slug + '.md')
        content_type = article.pop('type')
        version = article.pop('version').strip()
        if collection == 'daily':
            if content_type != mode:
                raise ValueError('Invalid briefing type')
        elif content_type not in CONTENT_TYPES:
            raise ValueError('Invalid content type')
        elif content_type != 'news':
            article.update(type=content_type, version=version, verified=day, status='current', tested=False)
            if content_type in ('skills', 'plugins', 'mcp', 'open-source', 'tools'):
                article['project'] = digest(canonical(evidence[0]['url']))
        if collection == 'daily' and (profiles or related):
            raise ValueError('Briefings cannot write resource metadata')
        if profiles:
            profile = resource_profile(profiles[0], evidence, existing, day)
            if profile['id'] in existing_ids:
                raise ValueError('Use resourceUpdates to refresh an existing profile')
            article['resource'] = profile
            article['verified'] = day
            existing_ids.add(profile['id'])
        if related:
            article['resourceIds'] = sorted(set(related))
        if path.exists() or path in writes:
            raise ValueError(f'article already exists: {slug}')
        tags = (re.sub(r'[^a-z0-9]+', '-', tag.lower()).strip('-') for tag in article['tags'])
        article['tags'] = list(dict.fromkeys(tag for tag in tags if tag))
        article['published'] = now.isoformat(timespec='seconds')
        article['sources'] = [dict(title=item['title'], url=item['url']) for item in evidence]
        primary_links = {source['url'] for source in article['sources']}
        for item in evidence:
            for doc in item.get('documents', []):
                if doc['url'] in links and doc['url'] not in primary_links:
                    article['sources'].append(dict(title=doc['label'], url=doc['url']))
                    primary_links.add(doc['url'])
        # JSON scalar values are valid in YAML frontmatter.
        front = '\n'.join(f'{key}: {json.dumps(value, ensure_ascii=False)}' for key, value in article.items())
        writes[path] = f'---\n{front}\n---\n{body.strip()}\n'
    updates = response.get('resourceUpdates', [])
    if not conforms(updates, UPDATES) or len(updates) > limit or (updates and mode in ('daily', 'weekly')):
        raise ValueError('Invalid resource updates')
    for update in updates:
        story = next((story for story in articles if story.get('resource', {}).get('id') == update['id']), None)
        ids = set(update['itemIds'])
        if not story or not ids or not ids <= candidates.keys():
            raise ValueError('Unknown resource or update evidence')
        old = story['resource']
        row = resource_profile(update['resource'], [candidates[key] for key in ids], existing, day)
        if row['id'] != old['id']:
            raise ValueError('Resource update cannot change identity')
        path = Path('src/content/news') / (story['slug'] + '.md')
        if path in revisions:
            raise ValueError('Duplicate resource update')
        row = {**old, **row}
        revisions[path] = (path.read_text(), row)
        used.update(ids)
    skipped = set(response['skipped'])
    if not skipped <= candidates.keys() or skipped & used:
        raise ValueError('invalid skipped candidate IDs')
    created = []
    changed = []
    try:
        for path, markdown in writes.items():
            with path.open('x') as handle:
                created.append(path)
                handle.write(markdown)
        for path, (original, resource) in revisions.items():
            revised = update_frontmatter(original, resource)
            if revised != original:
                changed.append(path)
                path.write_text(revised)
        metadata()
    except BaseException:
        for path in created:
            path.unlink(missing_ok=True)
        for path in changed:
            path.write_text(revisions[path][0])
        raise
    return skipped, {key for update in updates for key in update['itemIds']}


def edit(mode):
    items = load(ITEMS, {})
    articles = metadata()
    sync(items, articles)
    now = datetime.now(DATE_ZONE)
    day = now.date().isoformat()
    for entry in items.values():
        if entry['status'] == 'pending' and not entry.get('content_type') and timestamp(entry['published']) < now - timedelta(hours=48):
            entry['status'] = 'expired'
    save(ITEMS, items)
    if mode == 'daily' and any(story['collection'] == 'daily' and story['slug'] == day for story in articles):
        print('Daily briefing already exists')
        return
    candidates = choose(mode, items, now)
    if not candidates:
        print('No new candidates for the editorial window')
        return
    payload = json.dumps(dict(mode=mode, date=day, candidates=candidates, existingResources=resource_context(articles)), ensure_ascii=False)
    response = invoke(Path('ops/editor.md').read_text() + '\n\n' + payload, day, candidates)
    if response is None:
        return
    skipped, refreshed = write_articles(response, mode, candidates, now)
    sync(items, metadata())
    for key in refreshed:
        items[key]['status'] = 'published'
    for key in skipped:
        if items[key]['status'] == 'pending':
            items[key]['status'] = 'skipped'
    save(ITEMS, items)
