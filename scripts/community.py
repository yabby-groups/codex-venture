"""Normalize public community results into leads with primary-source links."""

import json
from urllib.parse import urlencode, urlsplit


def hn_rows(body):
    for row in json.loads(body)['hits']:
        if row.get('title') and row.get('objectID'):
            discussion = 'https://news.ycombinator.com/item?id=' + row['objectID']
            yield (row['title'], row.get('url') or discussion, row['created_at'],
                   row.get('story_text') or row['title'],
                   {'discussion': discussion, 'hn_id': row['objectID']})


def bluesky_rows(body):
    payload = json.loads(body)
    for row in payload.get('posts', payload.get('feed', [])):
        post = row.get('post', row)
        record = post['record']
        text = record.get('text')
        if not text:
            continue
        uri = post['uri']
        link = 'https://bsky.app/profile/' + post['author']['did'] + '/post/' + uri.rsplit('/', 1)[1]
        embed = record.get('embed', {}).get('external', {}).get('uri')
        if embed and urlsplit(embed).scheme != 'https':
            embed = None
        yield (text.splitlines()[0], embed or link, record.get('createdAt'), text,
               {'discussion': link, 'bsky_uri': uri})


def dev_rows(body):
    for row in json.loads(body):
        if row.get('title') and row.get('description'):
            yield (row['title'], row['url'], row['published_at'], row['description'])


def sources(slot):
    queries = (
        ('AI workflow', 'Agent Skills', 'AI 自動化'),
        ('Claude Code', 'AI coding', '本地模型'),
        ('Local LLM', 'AI inference', 'AI 動画'),
        ('MCP', 'Codex', 'AI startup'),
    )
    for index, query in enumerate(queries[slot % len(queries)]):
        yield dict(id=f'hacker-news-{slot}-{index}', kind='discovery', category='coding',
                   content_type='stories', parse=hn_rows,
                   url='https://hn.algolia.com/api/v1/search_by_date?' +
                   urlencode(dict(query=query, tags='story', hitsPerPage=12)))
        yield dict(id=f'bsky-search-{slot}-{index}', kind='discovery', category='agents',
                   content_type='stories', parse=bluesky_rows, enabled=False,
                   url='https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts?' +
                   urlencode(dict(q=query, sort='latest', limit=12)))
    for tag in ('ai', 'machinelearning', 'opensource', 'automation', 'tutorial'):
        yield dict(id='dev-' + tag, kind='discovery', category='coding',
                   content_type='tutorials', parse=dev_rows, interval_hours=20,
                   url='https://dev.to/api/articles?' + urlencode(dict(tag=tag, per_page=12)))
