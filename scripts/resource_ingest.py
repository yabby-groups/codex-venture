"""Discover and edit independent resources using the existing hosted trust boundary."""
import http.client
import json
import re
import time
from pathlib import Path
from urllib.parse import quote, urlencode

from article_schema import STRING, array, conforms, object_schema
from collect import canonical, clean, digest, fetch, load, save
from evidence import document, record, skill_files
from resource_editor import DIRECTORY, resource_context

STATE = Path('.venture-runtime/resources.json')
TYPES = ('skills', 'plugins', 'mcp', 'tools', 'models', 'open-source', 'resources', 'prompts', 'workflows')
REGISTRY = 'https://registry.modelcontextprotocol.io/v0.1/servers'
SKILL_REPOS = ('openai/skills', 'anthropics/skills', 'vercel-labs/agent-skills', 'huggingface/skills')
SCHEMA = object_schema(resources=array(object_schema(key=STRING, zh=STRING, en=STRING,
                                                    categoryZh=STRING, categoryEn=STRING)),
                       skipped=array(STRING))


def candidate(kind, identity, name, site, summary, source, **fields):
    if not name or not summary:
        return None
    return dict(type=kind, identity=identity, name=clean(name)[:120], site=canonical(site),
                description=clean(summary)[:1600], verificationSources=[canonical(source)],
                **{key: value for key, value in fields.items() if value})


def page(kind, feed, cursor):
    if kind == 'mcp':
        params = {'version': 'latest', 'limit': 40}
        if cursor:
            params['cursor'] = cursor
        data = json.loads(document(REGISTRY + '?' + urlencode(params)))
        rows = []
        for entry in data['servers']:
            server = entry['server']
            official = entry.get('_meta', {}).get('io.modelcontextprotocol.registry/official', {})
            if official.get('status') != 'active' or not official.get('isLatest'):
                continue
            name, version = server['name'], server['version']
            url = REGISTRY + '/' + quote(name, safe='') + '/versions/' + quote(version, safe='')
            transport = sorted({row['type'] for row in
                                [*server.get('remotes', []), *(p.get('transport', {}) for p in server.get('packages', []))]
                                if row.get('type')})
            rows.append(candidate(kind, 'mcp:' + name, server.get('title') or name, url,
                                  server.get('description'), url, version=version, registryId=name,
                                  transport=', '.join(transport)))
        return rows, data.get('metadata', {}).get('nextCursor')
    if kind == 'plugins':
        offset = int(cursor or 0)
        url = 'https://open-vsx.org/api/-/search?' + urlencode(dict(query=feed, size=25, offset=offset))
        data = json.loads(document(url))
        rows = []
        for extension in data['extensions']:
            if extension.get('deprecated'):
                continue
            publisher, name = extension['namespace'], extension['name']
            api = f'https://open-vsx.org/api/{publisher}/{name}/{extension["version"]}'
            site = f'https://open-vsx.org/extension/{publisher}/{name}'
            rows.append(candidate(kind, f'openvsx:{publisher}.{name}'.lower(),
                                  extension.get('displayName') or name, site, extension.get('description'),
                                  url, version=extension['version'], platforms=['Open VSX'], install=site,
                                  metadataUrl=api))
        return rows, offset + 25 if offset + 25 < data['totalSize'] else None
    if kind == 'models':
        url = cursor or 'https://huggingface.co/api/models?' + urlencode(
            dict(pipeline_tag=feed, sort='downloads', direction=-1, limit=30, full='true'))
        if not url.startswith('https://huggingface.co/api/models?'):
            raise ValueError('Invalid Hugging Face pagination URL')
        body, headers = fetch(url, {})
        rows = []
        for model in json.loads(body):
            if model.get('private') or model.get('disabled'):
                continue
            name = model['id']
            site = 'https://huggingface.co/' + name
            api = 'https://huggingface.co/api/models/' + name
            rows.append(candidate(kind, 'hf:' + name.lower(), name, site,
                                  (model.get('cardData') or {}).get('summary') or
                                  f'Hugging Face model listing for {name}. Pipeline: {model.get("pipeline_tag", feed)}.',
                                  url, metadataUrl=api, tags=[feed]))
        next_url = re.search(r'<([^>]+)>;\s*rel="next"', headers.get('Link', ''))
        return rows, next_url[1] if next_url else None
    page_number = int(cursor or 1)
    url = 'https://api.github.com/search/repositories?' + urlencode(
        dict(q=f'topic:{feed} archived:false fork:false', sort='stars', per_page=30, page=page_number))
    data = json.loads(document(url))
    rows = []
    for repo in data['items']:
        license_id = (repo.get('license') or {}).get('spdx_id')
        if kind == 'open-source' and license_id in (None, 'NOASSERTION'):
            continue
        site = repo['html_url']
        rows.append(candidate(kind, 'github:' + str(repo['id']), repo['full_name'], site,
                              repo.get('description'), url, repository=site, repositoryId=str(repo['id']),
                              license=license_id, metadataUrl=repo['url']))
    return rows, page_number + 1 if page_number * 30 < min(data['total_count'], 990) else None


FEEDS = {
    'plugins': ('AI assistant', 'coding assistant', 'language model', 'Claude', 'Copilot'),
    'mcp': ('registry',),
    'models': ('text-generation', 'image-text-to-text', 'text-to-image', 'text-to-video',
               'automatic-speech-recognition', 'text-to-speech', 'image-to-3d'),
    'open-source': ('ai-agents', 'llm-inference', 'text-to-speech', 'image-generation', 'video-generation'),
    'tools': ('ai-coding', 'rag', 'ai-automation', 'ai-design'),
    'prompts': ('prompt-templates',),
    'workflows': ('ai-workflow',),
    'resources': ('machine-learning-course', 'ai-education'),
}


def discover(queue, kind, day, refresh=False):
    tasks = [(name, feed) for name in TYPES if kind in ('all', name)
             for feed in (SKILL_REPOS if name == 'skills' else FEEDS[name])]
    deadline = time.monotonic() + 85
    feeds = queue.setdefault('feeds', {})
    for name, feed in sorted(tasks, key=lambda task: feeds.get(':'.join(task), {}).get('attempt', 0)):
        if time.monotonic() >= deadline:
            break
        state = feeds.setdefault(f'{name}:{feed}', {})
        if not refresh and state.get('complete') and day < state['complete']:
            continue
        state['attempt'] = time.time()
        try:
            if name == 'skills':
                item = state.setdefault('item', dict(discovery={}, source='github-skills',
                                                    category='agents', published=day))
                for _, skill in skill_files(item, feed, deadline):
                    info = skill['discovery']
                    row = candidate(name, f"github-skill:{info['repository_id']}:{info['skill_path']}",
                                    skill['title'], skill['url'], skill['summary'], skill['url'],
                                    repository='https://github.com/' + info['repository'],
                                    repositoryId=str(info['repository_id']), sourcePath=info['skill_path'],
                                    evidence=skill['evidence'][0]['excerpt'],
                                    platforms={'openai/skills': ['Codex'], 'anthropics/skills': ['Claude']}.get(feed))
                    enqueue(queue, row, day)
                    save(STATE, queue)
                next_cursor = True if item['skill_scan']['pending'] else None
            else:
                rows, next_cursor = page(name, feed, state.get('cursor'))
                for row in rows:
                    enqueue(queue, row, day)
            state['cursor'] = next_cursor
            if next_cursor is None:
                from datetime import date, timedelta
                state['complete'] = (date.fromisoformat(day) + timedelta(days=7)).isoformat()
        except (OSError, ValueError, KeyError, http.client.HTTPException) as error:
            print(f'{name}/{feed}: {type(error).__name__}: {error}', flush=True)
        save(STATE, queue)


def enqueue(queue, row, day):
    if not row or not row['name'] or not row['description']:
        return
    key = digest(row['type'] + ':' + row['identity'])
    rows = queue.setdefault('rows', {})
    old = rows.get(key, {})
    signature = digest(json.dumps({field: value for field, value in row.items()
                                   if field != 'verificationSources'}, sort_keys=True))
    if old.get('signature') == signature:
        return
    row['signature'] = signature
    row['firstDiscoveredAt'] = old.get('firstDiscoveredAt', day)
    rows[key] = row


def find_existing(row, existing):
    for entry in existing:
        if entry['type'] != row['type']:
            continue
        if entry.get('identity') == row['identity'] or canonical(entry['site']) == canonical(row['site']):
            return entry
        if row['type'] == 'mcp' and canonical(entry['site']).split('/versions/')[0] == canonical(row['site']).split('/versions/')[0]:
            return entry
    return None


def prepare(task, kind, day):
    if kind not in ('all', *TYPES):
        raise ValueError('Unknown resource type')
    queue = load(STATE, {})
    if task != 'resource-enrich':
        discover(queue, kind, day, refresh=task == 'resource-refresh')
    if task == 'resource-discover':
        return {}
    deadline = time.monotonic() + 65
    existing = resource_context()
    candidates = {}
    for key, row in sorted(queue.get('rows', {}).items(), key=lambda pair: (
            pair[1].get('attempt', 0), pair[1]['firstDiscoveredAt'], pair[0])):
        if len(candidates) >= 12 or time.monotonic() >= deadline:
            break
        if row.get('done') or kind not in ('all', row['type']):
            continue
        old = find_existing(row, existing)
        if old and not old.get('identity') and row['type'] == 'skills':
            row['done'] = 'already-published'
            continue
        row['attempt'] = time.time()
        try:
            if 'evidence' not in row:
                url = row.get('metadataUrl')
                if row['type'] == 'models':
                    url = row['site'] + '/raw/main/README.md'
                elif row.get('repository'):
                    url = row['metadataUrl'] + '/readme'
                if url:
                    evidence = document(url, plain=True, accept='application/vnd.github.raw+json'
                                        if row.get('repository') else None)
                    if row['type'] == 'plugins':
                        details = json.loads(evidence)
                        license_id = details.get('license')
                        if isinstance(license_id, str):
                            row['license'] = license_id
                    row['evidence'] = record(url, 'Publisher documentation', evidence)['excerpt']
                    row['verificationSources'] = [url]
                else:
                    details = json.loads(document(row['site']))
                    row['evidence'] = json.dumps(details, ensure_ascii=False)[:1900]
            if row['evidence'].strip():
                candidates[key] = {field: value for field, value in row.items() if field not in ('attempt', 'signature')}
        except (OSError, ValueError, KeyError, http.client.HTTPException) as error:
            print(f'{row["type"]}/{key[:10]}: {type(error).__name__}: {error}', flush=True)
    save(STATE, queue)
    return candidates


def publish(response, candidates, day):
    if not conforms(response, SCHEMA):
        raise ValueError('Invalid resource edit response')
    selected = [row['key'] for row in response['resources']] + response['skipped']
    if len(set(selected)) != len(selected) or not set(selected) <= candidates.keys():
        raise ValueError('Invalid resource candidate keys')
    queue = load(STATE, {})
    existing = resource_context()
    writes = {}
    for edit in response['resources']:
        key = edit['key']
        source = candidates[key]
        for field in ('zh', 'en', 'categoryZh', 'categoryEn'):
            value = edit[field].strip()
            pattern = r'[\u3400-\u9fff]' if field.lower().endswith('zh') else r'[A-Za-z]{2}'
            if not re.search(pattern, value) or len(value) > (650 if len(field) == 2 else 70) or re.search(r'[<>\x00-\x1f]', value):
                raise ValueError('Invalid bilingual resource copy')
        old = find_existing(source, existing)
        resource_id = old['id'] if old else 'resource-' + digest(source['type'] + ':' + source['identity'])
        row = {field: value for field, value in source.items()
               if field not in ('description', 'evidence', 'metadataUrl')}
        row = {**(old or {}), **row, 'id': resource_id, 'tested': False, 'verifiedAt': day,
               'summary': [edit['zh'].strip(), edit['en'].strip()],
               'categories': [[edit['categoryZh'].strip(), edit['categoryEn'].strip()]],
               'addedAt': old['addedAt'] if old else day}
        row['verificationSources'] = sorted(set(row['verificationSources']) |
                                            set((old or {}).get('verificationSources', [])))
        if old:
            row['updatedAt'] = day
        path = DIRECTORY / f'{resource_id}.json'
        writes[path] = row
        existing.append(row)
    for path, row in writes.items():
        save(path, row)
    for key in selected:
        queue['rows'][key]['done'] = 'published' if key not in response['skipped'] else 'declined'
    save(STATE, queue)
    return len(writes)
