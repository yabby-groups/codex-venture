import json
import re
from datetime import datetime, timedelta, timezone
from urllib.parse import urlencode, quote
from pathlib import Path

from community import hn_rows, sources as community_sources

from collect import collect, feed_rows, fetch, load, save


def github_row(repo, details=None):
    description = repo.get('description') or ''
    license_id = (repo.get('license') or {}).get('spdx_id')
    info = dict(repository=repo['full_name'], repository_id=repo['id'],
                created=repo['created_at'], updated=repo['updated_at'],
                stars=repo['stargazers_count'])
    info.update(details or {})
    return (repo['full_name'], repo['html_url'], repo['pushed_at'],
            f'{description} License: {license_id or "unknown"}.', info)


def github_rows(body):
    for repo in json.loads(body)['items'][:14]:
        if repo.get('description') and not repo['fork']:
            yield github_row(repo)


def hf_rows(kind):
    def rows(body):
        for row in json.loads(body)[:16]:
            repo = row['id']
            metadata = row.get('cardData') or {}
            path = '' if kind == 'models' else kind + '/'
            date = row.get('lastModified') or row.get('createdAt')
            summary = metadata.get('summary') or f'{kind} listing. Tags: {", ".join(row.get("tags") or [])}'
            yield (repo, 'https://huggingface.co/' + path + repo, date, summary,
                   {'hf_kind': kind, 'repository': repo})
    return rows


def arxiv_rows(body):
    for title, url, published, summary in feed_rows(body):
        if url and url.startswith('http://arxiv.org/'):
            url = 'https://' + url[len('http://'):]
        yield title, url, published, summary


def open_vsx_rows(body):
    for extension in json.loads(body)['extensions']:
        publisher, name = extension['namespace'], extension['name']
        if not extension.get('deprecated') and extension.get('description'):
            yield (extension.get('displayName') or name, f'https://open-vsx.org/extension/{publisher}/{name}',
                   extension['timestamp'], f"Open VSX version {extension['version']}. Publisher description: {extension['description']}",
                   {'open_vsx': f'https://open-vsx.org/api/{publisher}/{name}'})


def registry_rows(body):
    for entry in json.loads(body)['servers']:
        server = entry['server']
        official = entry['_meta']['io.modelcontextprotocol.registry/official']
        repo = server.get('repository', {}).get('url', '')
        if official.get('isLatest') and official['status'] == 'active':
            yield (server['name'], 'https://registry.modelcontextprotocol.io/v0.1/servers/' + quote(server['name'], safe='') + '/versions/' + quote(server['version'], safe=''), official['publishedAt'],
                   f"Registry listing {server['version']}. Publisher description: {server['description']}",
                   {'upstream': repo, 'registry_version': server['version']})


def discovery(days=7):
    start = (datetime.now(timezone.utc) - timedelta(days=days)).date()
    sources = []
    topics = ('ai-agents', 'mcp', 'llm', 'text-to-speech', 'image-generation',
              'video-generation', '3d', 'inference', 'ai-coding', 'agent-skills')
    offset = datetime.now(timezone.utc).date().toordinal() % len(topics)
    for index in range(3):
        topic = topics[(offset + index) % len(topics)]
        field = 'created' if index == 0 else 'pushed'
        stars = 'stars:1..50' if index == 0 else 'stars:>=10'
        query = urlencode({'q': f'topic:{topic} {field}:>={start} archived:false {stars}',
                           'sort': 'updated' if index == 0 else 'stars', 'per_page': 14})
        sources.append(dict(id=f'github-search-{topic}', kind='discovery', category='open-source',
                            url='https://api.github.com/search/repositories?' + query, parse=github_rows))
    now = datetime.now(timezone.utc)
    questions = (
        ('local-documents', 'local document assistant'),
        ('coding-cost', 'llm token cost'),
        ('creative-video', 'ai video editing'),
        ('personal-workflows', 'ai personal automation'),
        ('coding-workflows', 'agent coding workflow'),
        ('local-workstations', 'local llm workstation'),
    )
    direction, search = questions[now.date().toordinal() % len(questions)]
    query = urlencode({'q': f'{search} in:name,description pushed:>={start} archived:false',
                       'sort': 'updated', 'per_page': 12})
    sources.append(dict(id=f'planned-{direction}', kind='discovery', category='open-source',
                        interval_hours=20, url='https://api.github.com/search/repositories?' + query,
                        parse=github_rows))
    slot = (now.hour // 6) % 4
    for kind in ('models', 'datasets', 'spaces'):
        sources.append(dict(id='hf-' + kind, kind='discovery', category='models',
                            parse=hf_rows(kind), interval_hours=10,
                            url=f'https://huggingface.co/api/{kind}?sort=lastModified&direction=-1&limit=16&full=true'))
    sources.extend(community_sources(slot))
    sources.extend(trending_sources(now))
    for repo in ('openai/skills', 'anthropics/skills'):
        sources.append(dict(id='skills-' + repo.split('/')[0], kind='discovery', category='agents',
                            content_type='skills', interval_hours=20,
                            url='https://api.github.com/repos/' + repo,
                            parse=lambda body: (github_row(json.loads(body)),)))
    sources.append(dict(id='arxiv-ai', kind='discovery', category='models', parse=arxiv_rows,
                        interval_hours=20, url='https://rss.arxiv.org/rss/cs.AI'))
    keywords = ('automation', 'documents', 'testing', 'video', 'design', 'research', 'data')
    keyword = keywords[datetime.now(timezone.utc).date().toordinal() % len(keywords)]
    skill_query = urlencode({'q': f'agent-skills {keyword} in:name,description,readme archived:false',
                             'sort': 'updated', 'per_page': 10})
    registry_query = urlencode({'version': 'latest', 'limit': 12, 'search': keyword})
    extension_query = urlencode({'query': f'AI {keyword}', 'size': 10})
    sources.extend([
        dict(id='ecosystem-skill-search', kind='discovery', category='agents', content_type='skills', interval_hours=10,
             url='https://api.github.com/search/repositories?' + skill_query, parse=github_rows),
        dict(id='ecosystem-open-vsx', kind='discovery', category='coding', content_type='plugins', interval_hours=10,
             url='https://open-vsx.org/api/-/search?' + extension_query, parse=open_vsx_rows),
        dict(id='ecosystem-mcp-registry', kind='discovery', category='agents', content_type='mcp', interval_hours=10,
             url='https://registry.modelcontextprotocol.io/v0.1/servers?' + registry_query, parse=registry_rows),
        dict(id='ecosystem-show-hn', kind='discovery', category='coding', content_type='stories',
             url='https://hn.algolia.com/api/v1/search?query=AI&tags=show_hn&hitsPerPage=15', parse=hn_rows),
    ])
    return collect(days, sources, only_extra=True, refresh=days > 7)


def trending_sources(now):
    ranks = {}
    for period in ('daily', 'weekly', 'monthly'):
        try:
            body, _ = fetch('https://github.com/trending?since=' + period, {})
            links = re.findall(r'<h2[^>]*>\s*<a[^>]+href="/([\w.-]+/[\w.-]+)"', body.decode())
            for position, repo in enumerate(dict.fromkeys(links), 1):
                ranks.setdefault(repo, {})[period] = position
        except (OSError, ValueError) as error:
            print(f'GitHub Trending {period}: {error}', flush=True)

    path = Path('.venture-runtime/github-snapshots.json')
    snapshots = load(path, {})
    cutoff = (now - timedelta(days=35)).date().isoformat()
    snapshots = {key: {day: count for day, count in history.items() if day >= cutoff}
                 for key, history in snapshots.items() if any(day >= cutoff for day in history)}
    save(path, snapshots)
    pattern = re.compile(r'agent|\bai\b|llm|model|mcp|inference|speech|vision', re.I)

    def parser(positions):
        def rows(body):
            repo = json.loads(body)
            if not pattern.search(' '.join([repo.get('description') or '', *repo.get('topics', [])])):
                return
            day = now.date().isoformat()
            history = snapshots.setdefault(str(repo['id']), {})
            history[day] = repo['stargazers_count']
            prior = min(history)
            info = {'trending_ranks': positions, 'trending_checked': now.isoformat()}
            if prior < day:
                info.update(star_delta=history[day] - history[prior], star_delta_since=prior)
            save(path, snapshots)
            yield github_row(repo, info)
        return rows

    ranked = sorted(ranks, key=lambda repo: (min(ranks[repo].values()), -len(ranks[repo])))
    for repo in ranked[:18]:
        yield dict(id='trending-' + repo.lower().replace('/', '-'), kind='discovery',
                   category='open-source', url='https://api.github.com/repos/' + repo,
                   parse=parser(ranks[repo]), check_without_validators=True)
