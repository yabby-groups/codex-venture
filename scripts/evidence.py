"""Turn approved public documents into bounded editorial evidence."""

import json
import http.client
import re
import subprocess
import time
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, urlsplit

from collect import canonical, clean, digest, fetch, load, save, timestamp


class ArticleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.blocked = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('main', 'article'):
            self.depth += 1
        if tag in ('script', 'style', 'nav', 'footer', 'aside'):
            self.blocked += 1

    def handle_endtag(self, tag):
        if tag in ('main', 'article'):
            self.depth = max(0, self.depth - 1)
        if tag in ('script', 'style', 'nav', 'footer', 'aside'):
            self.blocked = max(0, self.blocked - 1)

    def handle_data(self, data):
        if self.depth and not self.blocked and data.strip():
            self.parts.append(data.strip())


GITHUB_DOCS = Path('.venture-runtime/github-documents.json')


def document(url, plain=False, accept=None):
    url = canonical(url)
    request_headers = {'Accept': accept} if accept else {}
    parts = urlsplit(url)
    cacheable = (parts.netloc == 'api.github.com' and parts.path.startswith('/repos/')
                 and '/git/blobs/' not in parts.path and '/git/trees/' not in parts.path)
    cache = load(GITHUB_DOCS, {}) if cacheable else {}
    key = digest(json.dumps([url, plain, accept]))
    cached = cache.get(key, {})
    checked = time.time()
    if cached:
        if checked - cached['checked'] < 21600:
            return cached['text']
        request_headers.update(cached['validators'])
    body, headers = fetch(url, request_headers)
    if body is None and cached:
        cached['checked'] = checked
        save(GITHUB_DOCS, cache)
        return cached['text']
    content_type = headers.get('Content-Type', '')
    if not any(kind in content_type for kind in ('text/', 'json', 'github.raw', 'octet-stream')):
        raise ValueError('unsupported evidence media type')
    text = body.decode('utf-8', errors='replace')
    if 'html' in content_type and not plain:
        parser = ArticleText()
        parser.feed(text)
        text = ' '.join(parser.parts)
    if cacheable and len(text.encode()) <= 64000:
        validators = {request: headers[response] for request, response in
                      [('If-None-Match', 'ETag'), ('If-Modified-Since', 'Last-Modified')]
                      if response in headers}
        cache[key] = dict(text=text, validators=validators, checked=checked)
        save(GITHUB_DOCS, dict(sorted(cache.items(), key=lambda item: item[1]['checked'])[-64:]))
    return text


def excerpt(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    relevant = [
        index for index, line in enumerate(lines)
        if re.match(r'^#{1,6}\s', line)
        and re.search(r'install|usage|example|require|config|license|limit|result|permission|depend|compatib', line, re.I)
    ]
    selected = lines[:10]
    for index in relevant[:8]:
        selected.extend(lines[index:index + 4])
    return '\n'.join(dict.fromkeys(selected))[:1900]


def record(url, label, text):
    return dict(url=canonical(url), label=label, excerpt=excerpt(text))


def github_root(item):
    details = item.get('discovery', {})
    candidate = details.get('upstream') or item['url']
    parts = urlsplit(candidate)
    match = re.match(r'^/([\w.-]+/[\w.-]+)(?:/releases(?:/|$)|/?$)', parts.path)
    return match[1] if parts.netloc == 'github.com' and match else None


def github_evidence(item, repo):
    api = 'https://api.github.com/repos/' + repo
    accept = 'application/vnd.github.raw+json'
    for label, path in (('README', '/readme'), ('LICENSE', '/license')):
        try:
            text = document(api + path, plain=True, accept=accept)
            yield record(api + path, label, text)
        except (OSError, ValueError, http.client.HTTPException):
            continue


def evidence_for(item):
    details = item.get('discovery', {})
    repo = github_root(item)
    if repo:
        yield from github_evidence(item, repo)
    if details.get('hf_kind'):
        prefix = {'models': '', 'datasets': 'datasets/', 'spaces': 'spaces/'}[details['hf_kind']]
        path = prefix + quote(details['repository'], safe='/')
        link = f'https://huggingface.co/{path}/raw/main/README.md'
        yield record(link, 'Model, dataset or Space card', document(link, plain=True))
    elif details.get('open_vsx'):
        link = details['open_vsx']
        data = json.loads(document(link))
        fields = {key: data.get(key) for key in (
            'name', 'version', 'description', 'engines', 'license', 'repository', 'timestamp'
        )}
        yield record(link, 'Publisher extension metadata', json.dumps(fields, ensure_ascii=False))
        readme = data.get('files', {}).get('readme')
        if readme:
            yield record(readme, 'Extension README', document(readme))
    elif details.get('registry_version'):
        link = item['url']
        yield record(link, 'Publisher server manifest', document(link))
    elif not repo or '/releases/' in item['url']:
        link = item['url']
        yield record(link, 'Original publication', document(link))

    if details.get('github_issue'):
        link = details['github_issue']
        if re.fullmatch(r'https://api.github.com/repos/openai/codex/issues/[0-9]+', link):
            issue = json.loads(document(link))
            author = issue.get('user', {}).get('login', '')
            yield record(item['url'], 'Public issue report and resolution status',
                         f"Author: {author}. State: {issue.get('state')}. "
                         f"State reason: {issue.get('state_reason')}. " + (issue.get('body') or ''))

    if details.get('hn_id', '').isdigit():
        link = 'https://hn.algolia.com/api/v1/items/' + details['hn_id']
        thread = json.loads(document(link))
        comments = [clean(child.get('text'))[:340] for child in thread.get('children', [])[:5]]
        yield record(link, 'Community discussion, unverified author claims', '\n'.join(filter(None, comments)))


def skill_index(base, branch, state, deadline):
    if 'tree_queue' not in state:
        tree = json.loads(document(base + '/git/trees/' + branch + '?recursive=1'))
        if not tree.get('truncated'):
            return {row['path']: row['sha'] for row in tree['tree']
                    if row['type'] == 'blob' and row['path'].split('/')[-1] == 'SKILL.md'}
        state.update(tree_queue=[['', tree.get('sha') or branch]], tree_paths={})
    remaining, paths = state['tree_queue'], state['tree_paths']
    while remaining:
        if time.monotonic() >= deadline:
            return None
        prefix, sha = remaining[-1]
        node = json.loads(document(base + '/git/trees/' + sha))
        if node.get('truncated'):
            raise ValueError('GitHub truncated a nonrecursive tree')
        remaining.pop()
        for row in node['tree']:
            path = prefix + row['path']
            if row['type'] == 'tree':
                remaining.append([path + '/', row['sha']])
            elif row['type'] == 'blob' and row['path'] == 'SKILL.md':
                paths[path] = row['sha']
    del state['tree_queue'], state['tree_paths']
    return paths


def skill_metadata(text):
    return json.loads(subprocess.check_output(
        ['node', 'scripts/skill-frontmatter.mjs'], input=text, text=True, timeout=10))


def skill_files(item, repo, deadline):
    state = item.setdefault('skill_scan', {})
    if not state.get('pending'):
        data = json.loads(document('https://api.github.com/repos/' + repo))
        base = 'https://api.github.com/repos/' + data['full_name']
        branch = quote(data['default_branch'], safe='')
        paths = skill_index(base, branch, state, deadline)
        if paths is None:
            return
        seen = state.get('seen', {}) if (state.get('repo'), state.get('branch')) == (data['full_name'], branch) else {}
        state.update(repo=data['full_name'], branch=branch, repository_id=data['id'],
                     pending={path: sha for path, sha in sorted(paths.items())
                              if seen.get(path) != sha})
    base = 'https://api.github.com/repos/' + state['repo']
    for path, sha in list(state['pending'].items()):
        if time.monotonic() >= deadline:
            break
        escaped = quote(path, safe='/')
        public_url = f"https://github.com/{state['repo']}/blob/{state['branch']}/{escaped}"
        text = document(base + '/git/blobs/' + sha, plain=True, accept='application/vnd.github.raw+json')
        fields = skill_metadata(text)
        if fields.get('name') and fields.get('description'):
            key = digest(f"github-skill:{state['repository_id']}:{path}")
            discovery = {**item['discovery'], 'skill_path': path, 'repository_id': state['repository_id'],
                         'repository': state['repo'], 'blob': sha}
            skill = dict(url=public_url, title=fields['name'][:300], summary=fields['description'][:1200],
                         fingerprint=key, discovery=discovery, source=item['source'],
                         category=item['category'], published=item['published'], content_type='skills',
                         evidence=[record(public_url, 'Skill manifest', text)], status='pending')
            yield key, skill
        state.setdefault('seen', {})[path] = sha
        del state['pending'][path]


def enrich(items, candidates, now, limit=5):
    checked = now.astimezone(timezone.utc).isoformat()
    deadline = time.monotonic() + 75
    attempted = succeeded = 0
    for key in candidates:
        if attempted == limit or time.monotonic() >= deadline:
            break
        item = items[key]
        last = item.get('evidence_checked')
        scan = item.get('skill_scan', {})
        if last and not (scan.get('pending') or scan.get('tree_queue')) and now - timestamp(last) < timedelta(days=3 if item.get('evidence') else 1):
            continue
        attempted += 1
        documents = []
        try:
            if item.get('content_type') == 'skills' and not item.get('discovery', {}).get('skill_path'):
                repo = github_root(item)
                for skill_id, skill in skill_files(item, repo, deadline) if repo else ():
                    if skill_id in items:
                        skill['status'] = items[skill_id]['status']
                        if 'articles' in items[skill_id]:
                            skill['articles'] = items[skill_id]['articles']
                    skill['evidence_checked'] = checked
                    skill['verified_at'] = checked
                    items[skill_id] = skill
                    documents.extend(skill['evidence'])
                if item.get('skill_scan', {}).get('seen'):
                    item['status'] = 'superseded'
            else:
                for source in evidence_for(item):
                    if source['excerpt']:
                        documents.append(source)
        except (OSError, ValueError, KeyError, TypeError, http.client.HTTPException) as error:
            print(f'{key[:12]} evidence: {type(error).__name__}', flush=True)
        item['evidence_checked'] = checked
        if documents:
            item['evidence'] = documents[:4]
            item['verified_at'] = checked
            succeeded += 1
    return dict(evidence_attempted=attempted, evidence_succeeded=succeeded)
