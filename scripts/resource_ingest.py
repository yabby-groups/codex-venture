"""Discover and edit independent resources using the existing hosted trust boundary."""
from collection_budget import CollectionPaused
from collections import Counter
from datetime import date, timedelta
from itertools import zip_longest
import http.client
import json
import re
import time
from urllib.error import HTTPError
from pathlib import Path
from urllib.parse import quote, urlencode, urlsplit

from article_schema import STRING, array, conforms, object_schema
from collect import canonical, clean, digest, fetch, load, save
from evidence import document, record, skill_files
from resource_editor import DIRECTORY, resource_context

STATE = Path('.venture-runtime/resources.json')
TYPES = ('skills', 'plugins', 'mcp', 'tools', 'models', 'open-source', 'resources', 'prompts', 'workflows')
REGISTRY = 'https://registry.modelcontextprotocol.io/v0.1/servers'
SKILL_REPOS = (
    'openai/skills', 'anthropics/skills', 'vercel-labs/agent-skills', 'huggingface/skills',
    'microsoft/skills', 'google-gemini/gemini-cli', 'remotion-dev/skills',
)
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
        if feed.startswith('jetbrains:'):
            url = 'https://plugins.jetbrains.com/api/searchPlugins?' + urlencode(
                dict(search=feed.removeprefix('jetbrains:'), max=15))
            data = json.loads(document(url))
            rows = []
            for plugin in data['plugins']:
                if not plugin.get('vendor', {}).get('isVerified') or not plugin['link'].startswith('/plugin/'):
                    continue
                site = 'https://plugins.jetbrains.com' + plugin['link']
                rows.append(candidate(kind, f"jetbrains:{plugin['id']}", plugin['name'], site,
                                      plugin.get('preview'), site, platforms=['JetBrains Marketplace'], install=site))
            return rows, None
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
    'plugins': ('AI assistant', 'coding assistant', 'language model', 'Claude', 'Copilot', 'jetbrains:AI Assistant', 'jetbrains:Code Completion'),
    'mcp': ('registry',),
    'models': ('text-generation', 'image-text-to-text', 'text-to-image', 'text-to-video',
               'automatic-speech-recognition', 'text-to-speech', 'image-to-3d'),
    'open-source': ('ai-agents', 'llm-inference', 'text-to-speech', 'image-generation', 'video-generation'),
    'tools': ('ai-coding', 'rag', 'ai-automation', 'ai-design'),
    'prompts': ('prompt-templates',),
    'workflows': ('ai-workflow',),
    'resources': ('machine-learning-course', 'ai-education'),
}


OFFICIAL_DOCUMENTS = {
    'tools': {
        'Google AI Studio': 'https://ai.google.dev/gemini-api/docs/ai-studio-quickstart',
        'Perplexity': 'https://www.perplexity.ai/help-center/en/',
        'ElevenLabs': 'https://elevenlabs.io/docs/overview/intro',
        'NotebookLM': 'https://support.google.com/notebooklm/',
    },
    'resources': {
        'Hugging Face LLM Course': 'https://huggingface.co/learn/llm-course/chapter1/1',
        'Agent Skills Specification': 'https://agentskills.io/specification',
        'OpenAI Cookbook': 'https://cookbook.openai.com/',
        'MCP Architecture': 'https://modelcontextprotocol.io/docs/learn/architecture',
    },
    'prompts': {
        'Gemini Prompt Design Strategies': 'https://ai.google.dev/gemini-api/docs/prompting-strategies',
    },
    'workflows': {
        'GitHub Actions Workflow Syntax': 'https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions',
    },
}


def official_rows(kind):
    for name, url in OFFICIAL_DOCUMENTS.get(kind, {}).items():
        row = candidate(kind, 'url:' + canonical(url), name, url, name, url)
        row['metadataUrl'] = url
        yield row


def discover(queue, kind, day, refresh=False):
    tasks = [(name, feed) for name in TYPES if kind in ('all', name)
             for feed in (SKILL_REPOS if name == 'skills' else FEEDS[name])]
    for name in TYPES if kind == 'all' else (kind,):
        for row in official_rows(name):
            enqueue(queue, row, day)
    save(STATE, queue)
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
                scan = item['skill_scan']
                next_cursor = True if scan.get('pending') or scan.get('tree_queue') else None
            else:
                rows, next_cursor = page(name, feed, state.get('cursor'))
                for row in rows:
                    enqueue(queue, row, day)
            state['cursor'] = next_cursor
            if next_cursor is None:
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
    sources = sorted(set(row['verificationSources']) | set(old.get('verificationSources', [])))
    if old.get('signature') == signature:
        old['verificationSources'] = sources
        return
    rows[key] = {**row, 'signature': signature, 'verificationSources': sources,
                 'firstDiscoveredAt': old.get('firstDiscoveredAt', day)}


def find_existing(row, existing):
    for entry in existing:
        if entry['type'] != row['type']:
            continue
        if entry.get('identity') == row['identity'] or canonical(entry['site']) == canonical(row['site']):
            return entry
        if row['type'] == 'mcp' and canonical(entry['site']).split('/versions/')[0] == canonical(row['site']).split('/versions/')[0]:
            return entry
    return None


def structured_evidence(row):
    """Use publisher records already captured by discovery."""
    if row.get('evidence', '').strip():
        return row['evidence']
    if row['identity'].startswith(('github:', 'openvsx:', 'jetbrains:', 'mcp:', 'hf:')):
        description = row['description']
        if not description.startswith('Hugging Face model listing for '):
            return description
    return ''


def editorial_input(candidates):
    compact = {}
    for key, row in candidates.items():
        entry = dict(name=row['name'], type=row['type'], description=row['description'])
        if row['evidence'] != row['description']:
            entry['excerpt'] = row['evidence'][:1900]
        for field in ('platforms', 'transport'):
            if row.get(field):
                entry[field] = row[field]
        compact[key] = entry
    return compact


def prepare(task, kind, day, capacity=12, coverage=None):
    if kind not in ('all', *TYPES):
        raise ValueError('Unknown resource type')
    queue = load(STATE, {})
    pending_count = sum(not row.get('done') and kind in ('all', row['type'])
                        for row in queue.get('rows', {}).values())
    if task != 'resource-enrich' and (task != 'resource-sync' or pending_count < capacity * 2):
        discover(queue, kind, day, refresh=task == 'resource-refresh')
    if task == 'resource-discover':
        return {}
    deadline = time.monotonic() + 65
    existing = resource_context()
    candidates = {}
    pending = {name: [] for name in TYPES}
    counts = Counter()
    for key, row in sorted(queue.get('rows', {}).items(), key=lambda pair: (
            pair[1].get('attempt', 0), pair[1]['firstDiscoveredAt'], pair[0])):
        if not row.get('done') and kind in ('all', row['type']):
            pending[row['type']].append((key, row))
    order = sorted(pending, key=lambda name: (coverage or {}).get(name, 0))
    paused_hosts = set()
    for entry in (entry for group in zip_longest(*(pending[name] for name in order)) for entry in group if entry):
        key, row = entry
        if len(candidates) >= capacity or time.monotonic() >= deadline:
            break
        old = find_existing(row, existing)
        if old and (old.get('sourceSignature') == row.get('signature') or
                    (not old.get('identity') and row['type'] == 'skills')):
            row['done'] = 'already-published'
            continue
        row['attempt'] = time.time()
        needs_evidence = not row.get('evidence')
        counts['evidence_attempted'] += needs_evidence
        host = urlsplit(row.get('metadataUrl') or row['site']).hostname
        url = row.get('metadataUrl') or row['site']
        try:
            evidence = structured_evidence(row)
            if evidence:
                row['evidence'] = evidence
            else:
                url = row.get('metadataUrl') or row['site']
                if row['type'] == 'models':
                    url = row['site'] + '/raw/main/README.md'
                elif row.get('repository'):
                    url = row['metadataUrl'] + '/readme'
                host = urlsplit(url).hostname
                if host in paused_hosts:
                    continue
                if row.get('metadataUrl'):
                    evidence = document(url, plain=row['type'] in ('models', 'plugins') or bool(row.get('repository')), accept='application/vnd.github.raw+json'
                                        if row.get('repository') else None)
                    if row['type'] == 'plugins' and row['identity'].startswith('openvsx:'):
                        details = json.loads(evidence)
                        license_id = details.get('license')
                        if isinstance(license_id, str):
                            row['license'] = license_id
                    row['evidence'] = record(url, 'Publisher documentation', evidence)['excerpt']
                    row['verificationSources'] = sorted(set(row['verificationSources']) | {canonical(url)})
                else:
                    details = json.loads(document(row['site']))
                    row['evidence'] = json.dumps(details, ensure_ascii=False)[:1900]
            if row['evidence'].strip():
                counts['evidence_ready'] += needs_evidence
                candidates[key] = {field: value for field, value in row.items()
                                   if field not in ('attempt', 'missingChecks', 'editFailure')}
        except HTTPError as error:
            if error.code in (404, 410):
                row['missingChecks'] = sorted(set(row.get('missingChecks', [])) | {day})[-2:]
                if len(row['missingChecks']) == 2 and canonical(url) == canonical(row['site']):
                    row['done'] = 'unavailable'
                counts['missing_document'] += 1
            if error.code == 429 or (error.headers and error.headers.get('X-RateLimit-Remaining') == '0'):
                paused_hosts.add(host)
                counts['paused_hosts'] = len(paused_hosts)
            print(f'{row["type"]}/{key[:10]}: HTTP {error.code}', flush=True)
        except (OSError, ValueError, KeyError, http.client.HTTPException) as error:
            if isinstance(error, CollectionPaused):
                paused_hosts.add(error.host)
                counts['paused_hosts'] = len(paused_hosts)
            print(f'{row["type"]}/{key[:10]}: {type(error).__name__}: {error}', flush=True)
    save(STATE, queue)
    print('Resource preparation:', json.dumps(counts), flush=True)
    return candidates


def publish(response, candidates, day):
    if (type(response) is not dict or set(response) != {'resources', 'skipped'}
            or type(response['resources']) is not list or type(response['skipped']) is not list):
        raise ValueError('Invalid resource edit response')
    queue = load(STATE, {})
    existing = resource_context()
    writes = {}
    counts = {'added': 0, 'updated': 0, 'invalid': 0}
    keys = Counter(edit.get('key') for edit in response['resources']
                   if isinstance(edit, dict) and isinstance(edit.get('key'), str))
    keys.update(key for key in response['skipped'] if isinstance(key, str))
    accepted = {key for key in response['skipped']
                if isinstance(key, str) and key in candidates and keys[key] == 1}
    for edit in response['resources']:
        key = edit.get('key') if isinstance(edit, dict) else None
        valid_key = isinstance(key, str) and key in candidates
        if (not valid_key or keys[key] != 1
                or not conforms(edit, SCHEMA['properties']['resources']['items'])):
            counts['invalid'] += 1
            if valid_key:
                queue['rows'][key]['editFailure'] = 'invalid response fields or duplicate key'
            continue
        source = candidates[key]
        for field in ('zh', 'en', 'categoryZh', 'categoryEn'):
            value = edit[field].strip()
            pattern = r'[\u3400-\u9fff]' if field.lower().endswith('zh') else r'[A-Za-z]{2}'
            if not re.search(pattern, value) or len(value) > (650 if len(field) == 2 else 70) or re.search(r'[<>\x00-\x1f]', value):
                counts['invalid'] += 1
                queue['rows'][key]['editFailure'] = f'invalid {field}'
                print(f'Resource {key[:12]} needs revised {field}; kept in queue', flush=True)
                break
        else:
            accepted.add(key)
        if key not in accepted:
            continue
        old = find_existing(source, existing)
        resource_id = old['id'] if old else 'resource-' + digest(source['type'] + ':' + source['identity'])
        row = {field: value for field, value in source.items()
               if field not in ('description', 'evidence', 'metadataUrl', 'signature')}
        row = {**(old or {}), **row, 'id': resource_id,
               'tested': bool(old and old.get('tested') and old.get('version') == source.get('version')),
               'verifiedAt': day,
               'summary': [edit['zh'].strip(), edit['en'].strip()],
               'categories': [[edit['categoryZh'].strip(), edit['categoryEn'].strip()]],
               'addedAt': old['addedAt'] if old else day}
        row['verificationSources'] = sorted(set(row['verificationSources']) |
                                            set((old or {}).get('verificationSources', [])))
        if source.get('signature'):
            row['sourceSignature'] = source['signature']
        if old:
            row['updatedAt'] = day
        path = DIRECTORY / f'{resource_id}.json'
        counts['updated' if old else 'added'] += 1
        writes[path] = row
        if old:
            existing.remove(old)
        existing.append(row)
    for path, row in writes.items():
        save(path, row)
    for key in accepted:
        queue['rows'][key].pop('editFailure', None)
        queue['rows'][key]['done'] = 'published' if key not in response['skipped'] else 'declined'
    save(STATE, queue)
    return counts


def statistics(day):
    rows = resource_context()
    queue = load(STATE, {}).get('rows', {})
    pending = [row for row in queue.values() if not row.get('done')]
    return dict(
        total=len(rows),
        by_type=dict(Counter(row['type'] for row in rows)),
        added_today=sum(row['addedAt'] == day for row in rows),
        updated_today=sum(row.get('updatedAt') == day for row in rows),
        queued=len(pending),
        awaiting_evidence=sum(not row.get('evidence') for row in pending),
        awaiting_editor=sum(bool(row.get('evidence')) for row in pending),
        unavailable=sum(row.get('done') == 'unavailable' for row in queue.values()),
        edit_failures=sum(bool(row.get('editFailure')) for row in pending),
        oldest_pending=min((row['firstDiscoveredAt'] for row in pending), default=None),
        older_than_week=sum((date.fromisoformat(day) - date.fromisoformat(row['firstDiscoveredAt'])).days >= 7
                            for row in pending),
        duplicate_matches=sum(row.get('done') == 'already-published' for row in queue.values()),
    )
