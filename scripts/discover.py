import json
import re
from datetime import datetime, timedelta, timezone
from urllib.parse import urlencode

from collect import collect, feed_rows, fetch


def github_rows(body):
    for repo in json.loads(body)['items'][:10]:
        if repo['description'] and repo.get('license') and not repo['fork']:
            yield (repo['full_name'], repo['html_url'], repo['pushed_at'],
                   f"{repo['description']} License: {repo['license']['spdx_id']}.")


def hf_rows(body):
    for row in json.loads(body)[:12]:
        repo = row['id']
        metadata = row.get('cardData') or {}
        if metadata.get('summary') and row.get('lastModified'):
            yield (repo, 'https://huggingface.co/' + repo, row['lastModified'],
                   metadata['summary'])


def arxiv_rows(body):
    for title, url, published, summary in feed_rows(body):
        if url and url.startswith('http://arxiv.org/'):
            url = 'https://' + url[len('http://'):]
        yield title, url, published, summary


def hn_rows(body):
    for row in json.loads(body)['hits'][:20]:
        if row.get('url') and row.get('title'):
            # The discussion is a lead, not evidence about the linked product.
            yield (row['title'], 'https://news.ycombinator.com/item?id=' + row['objectID'],
                   row['created_at'], 'Community discussion. Linked source: ' + row['url'])


def discovery(days=7):
    start = (datetime.now(timezone.utc) - timedelta(days=days)).date()
    sources = []
    topics = ('ai-agents', 'mcp', 'llm', 'text-to-speech', 'image-generation',
              'video-generation', '3d', 'inference', 'ai-coding', 'agent-skills')
    offset = datetime.now(timezone.utc).date().toordinal() % len(topics)
    for index in range(3):
        topic = topics[(offset + index) % len(topics)]
        field = 'created' if index == 0 else 'pushed'
        query = urlencode({'q': f'topic:{topic} {field}:>={start} archived:false stars:>=25',
                           'sort': 'stars', 'per_page': 10})
        sources.append(dict(id=f'github-search-{topic}', kind='discovery', category='open-source',
                            url='https://api.github.com/search/repositories?' + query, parse=github_rows))
    repos = set()
    for period in ('daily', 'weekly', 'monthly'):
        try:
            body, _ = fetch('https://github.com/trending?since=' + period, {})
            for repo in re.findall(r'<h2[^>]*>\s*<a[^>]+href="/([\w.-]+/[\w.-]+)"', body.decode())[:10]:
                repos.add(repo)
        except (OSError, ValueError) as error:
            print(f'GitHub Trending {period}: {error}')
    topics_pattern = re.compile(r'agent|\bai\b|llm|model|mcp|inference|speech|vision', re.I)

    def trending_rows(body):
        repo = json.loads(body)
        return github_rows(json.dumps({'items': [repo] if topics_pattern.search(
            ' '.join([repo['description'] or '', *repo['topics']])) else []}))

    for repo in sorted(repos)[:12]:
        sources.append(dict(id='trending-' + repo.lower().replace('/', '-'), kind='discovery',
                            category='open-source', url='https://api.github.com/repos/' + repo,
                            parse=trending_rows))
    sources.extend([
        dict(id='hf-models', kind='discovery', category='models', parse=hf_rows,
             url='https://huggingface.co/api/models?sort=trendingScore&limit=12&full=true&cardData=true'),
        dict(id='hacker-news-ai', kind='discovery', category='coding', parse=hn_rows,
             url='https://hn.algolia.com/api/v1/search_by_date?query=AI&tags=story&hitsPerPage=20'),
        dict(id='product-hunt', kind='feed', category='open-source', url='https://www.producthunt.com/feed'),
        dict(id='arxiv-ai', kind='discovery', category='models', parse=arxiv_rows,
             url='https://rss.arxiv.org/rss/cs.AI'),
    ])
    return collect(days, sources, only_extra=True, refresh=days > 7)
