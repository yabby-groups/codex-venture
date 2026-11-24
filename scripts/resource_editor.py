"""Validate resource metadata in the existing editorial response."""
import json
import re
from urllib.parse import urlsplit

from article_schema import PAIR, STRING, array, conforms, enum, object_schema
from collect import canonical, digest

TYPES = ('skills', 'plugins', 'mcp', 'tools', 'models', 'open-source', 'prompts', 'workflows', 'resources')
OPTIONAL = ('nameZh', 'repository', 'license', 'install', 'transport', 'deployment', 'kind', 'version', 'releasedAt')
FIELDS = object_schema(type=enum(*TYPES), name=STRING, site=STRING, summary=PAIR,
                       platforms=array(STRING), categories=array(PAIR), **dict.fromkeys(OPTIONAL, STRING))
UPDATES = array(object_schema(id=STRING, itemIds=array(STRING), resource=FIELDS))
PROFILES = array(FIELDS)


def resource_context(articles):
    return [{key: row[key] for key in ('id', 'type', 'name', 'site', 'repository') if key in row}
            for article in articles if (row := article.get('resource'))]


def resource_profile(value, evidence, existing, day):
    if not conforms(value, FIELDS):
        raise ValueError('Invalid resource profile shape')
    if (not value['name'].strip() or not value['categories'] or
            any(not part.strip() for pair in [value['summary'], *value['categories']] for part in pair.values())):
        raise ValueError('Missing resource name or bilingual metadata')
    site = value['site']
    identity = canonical(site)
    sources = {canonical(item['url']) for item in evidence}
    old = next((row for row in existing if row['type'] == value['type'] and canonical(row['site']) == identity), None)
    evidence_prefix = (old or {}).get('repository', site).rstrip('/') + '/releases/'
    if identity not in sources and not (old and any(url.startswith(evidence_prefix) for url in sources)):
        raise ValueError('Resource identity lacks direct source evidence')
    repository = value['repository']
    if repository and canonical(repository) not in sources and repository != (old or {}).get('repository'):
        repo = urlsplit(repository)
        source = urlsplit(site)
        if repo.scheme != 'https' or repo.netloc != 'github.com' or source.netloc != repo.netloc or not (
            source.path.startswith(repo.path.rstrip('/') + '/')
        ):
            raise ValueError('Resource repository lacks source evidence')
    row = {key: value[key] for key in OPTIONAL if value[key]}
    row.update(id=old['id'] if old else 'resource-' + digest(value['type'] + ':' + identity),
               type=value['type'], name=value['name'], site=site, verifiedAt=day,
               verificationSources=sorted({item['url'] for item in evidence}),
               summary=[value['summary'][key] for key in ('zh', 'en')],
               categories=[[pair['zh'], pair['en']] for pair in value['categories']],
               platforms=list(dict.fromkeys(value['platforms'])))
    return row


def update_frontmatter(text, resource):
    front, body = text[4:].split('\n---\n', 1)
    replacement, count = re.subn(r'^resource: .+$', lambda _: 'resource: ' + json.dumps(
        resource, ensure_ascii=False), front, flags=re.M)
    if count != 1:
        raise ValueError('Resource updates require a single inline resource field')
    return '---\n' + replacement + '\n---\n' + body
