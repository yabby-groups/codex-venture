"""Turn approved public documents into bounded editorial evidence."""

import json
import http.client
import re
import time
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from urllib.parse import quote, urlsplit

from collect import canonical, clean, digest, fetch, timestamp


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


def document(url, plain=False, accept=None):
    body, headers = fetch(canonical(url), {'Accept': accept} if accept else {})
    content_type = headers.get('Content-Type', '')
    if not any(kind in content_type for kind in ('text/', 'json', 'github.raw', 'octet-stream')):
        raise ValueError('unsupported evidence media type')
    text = body.decode('utf-8', errors='replace')
    if 'html' in content_type and not plain:
        parser = ArticleText()
        parser.feed(text)
        text = ' '.join(parser.parts)
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

    if details.get('hn_id', '').isdigit():
        link = 'https://hn.algolia.com/api/v1/items/' + details['hn_id']
        thread = json.loads(document(link))
        comments = [clean(child.get('text'))[:340] for child in thread.get('children', [])[:5]]
        yield record(link, 'Community discussion, unverified author claims', '\n'.join(filter(None, comments)))


def skill_files(item, repo):
    base = 'https://api.github.com/repos/' + repo
    data = json.loads(document(base))
    branch = quote(data['default_branch'], safe='')
    tree = json.loads(document(base + '/git/trees/' + branch + '?recursive=1'))
    paths = sorted(row['path'] for row in tree.get('tree', [])
                   if row['type'] == 'blob' and row['path'].split('/')[-1] == 'SKILL.md')
    for path in paths[:6]:
        escaped = quote(path, safe='/')
        link = base + '/contents/' + escaped
        try:
            text = document(link, plain=True, accept='application/vnd.github.raw+json')
        except (OSError, ValueError, http.client.HTTPException):
            continue
        frontmatter = re.match(r'\A---\s*\n(.*?)\n---', text, flags=re.S)
        if not frontmatter:
            continue
        fields = dict(re.findall(r'(?m)^(name|description):[ \t]*(.*)$', frontmatter[1]))
        title = fields.get('name', '').strip(' \'"')
        description = fields.get('description', '').strip(' \'"')
        if not title or not description or description in ('|', '>'):
            continue
        public_url = f'https://github.com/{repo}/blob/{branch}/{escaped}'
        key = digest(f"github-skill:{data['id']}:{path}")
        discovery = {**item['discovery'], 'skill_path': path, 'repository_id': data['id']}
        yield key, {**item, 'url': public_url, 'title': title[:300], 'summary': description[:1200],
                    'fingerprint': key, 'discovery': discovery,
                    'evidence': [record(public_url, 'Skill manifest', text)], 'status': 'pending'}


def enrich(items, candidates, now, limit=5):
    checked = now.astimezone(timezone.utc).isoformat()
    deadline = time.monotonic() + 75
    attempted = succeeded = 0
    for key in candidates:
        if attempted == limit or time.monotonic() >= deadline:
            break
        item = items[key]
        last = item.get('evidence_checked')
        if last and now - timestamp(last) < timedelta(days=3 if item.get('evidence') else 1):
            continue
        attempted += 1
        documents = []
        try:
            if item.get('content_type') == 'skills' and not item.get('discovery', {}).get('skill_path'):
                repo = github_root(item)
                for skill_id, skill in skill_files(item, repo) if repo else ():
                    if skill_id in items:
                        skill['status'] = items[skill_id]['status']
                        if 'articles' in items[skill_id]:
                            skill['articles'] = items[skill_id]['articles']
                    skill['evidence_checked'] = checked
                    skill['verified_at'] = checked
                    items[skill_id] = skill
                    documents.extend(skill['evidence'])
                if documents:
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
