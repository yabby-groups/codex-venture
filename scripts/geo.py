"""Public GEO checks and private analytics aggregation."""
import re
from collections import Counter
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from xml.etree import ElementTree

SITE = 'https://codex-venture.com'
REFERRERS = {
    'chatgpt.com': 'ChatGPT', 'chat.openai.com': 'ChatGPT',
    'www.perplexity.ai': 'Perplexity', 'perplexity.ai': 'Perplexity',
    'copilot.microsoft.com': 'Copilot', 'gemini.google.com': 'Gemini',
    'claude.ai': 'Claude',
}
SEARCH_AGENTS = ('Googlebot', 'Bingbot', 'OAI-SearchBot', 'PerplexityBot')


def referral_totals(rows):
    counts = Counter()
    for row in rows:
        host = row.get('dimensions', {}).get('refererHost', '').lower().rstrip('.')
        counts[REFERRERS.get(host, 'unknown')] += row['count']
    return counts


def robot_groups(body, require_sitemap=False):
    groups = {}
    group = []
    has_rule = False
    sitemap = False
    for line in body.splitlines():
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        key, divider, value = line.partition(':')
        key, value = key.strip().lower(), value.strip()
        if not divider or not re.fullmatch(r'[a-z-]+', key):
            raise ValueError('Malformed robots directive')
        if key == 'user-agent':
            if has_rule:
                group = []
                has_rule = False
            if not re.fullmatch(r'\*|[a-zA-Z_-][a-zA-Z0-9_-]*', value):
                raise ValueError('Invalid robots User-agent')
            group.append(value.lower())
            groups.setdefault(value.lower(), [])
        elif key in ('allow', 'disallow'):
            if not group or (value and not value.startswith('/')):
                raise ValueError('Invalid robots path or missing User-agent')
            has_rule = True
            for agent in group:
                groups[agent].append((key, value))
        elif key == 'sitemap':
            sitemap |= value == SITE + '/sitemap-index.xml'
    if require_sitemap and not sitemap:
        raise ValueError('Missing production sitemap in robots.txt')
    for agent in ('*', *SEARCH_AGENTS):
        rules = groups.get(agent.lower(), groups.get('*', []))
        if ('allow', '/') not in rules or any(key == 'disallow' and path for key, path in rules):
            raise ValueError(f'Review search crawl policy for {agent}')
    return groups


def request(path, agent='CodexVenturePublicCheck/1.0', expected=200):
    url = SITE + path
    try:
        response = urlopen(Request(url, headers={'User-Agent': agent}), timeout=18)
    except HTTPError as error:
        response = error
    with response:
        print(f'{agent} {response.status} {path}')
        robots = response.headers.get('X-Robots-Tag', '').lower()
        if response.status != expected or response.url != url or response.headers.get('cf-mitigated'):
            raise ValueError(f'Unexpected public response for {path}')
        if expected == 200 and re.search(r'\b(noindex|nosnippet|none)\b', robots):
            raise ValueError(f'Unexpected X-Robots-Tag on {path}')
        return response.read(3_000_000).decode()


def probe():
    from check import Page

    robot_groups(request('/robots.txt'), require_sitemap=True)
    sitemap = ElementTree.fromstring(request('/sitemap-index.xml'))
    paths = [urlsplit(node.text).path for node in sitemap.findall('.//{*}loc')]
    if not paths:
        raise ValueError('Empty sitemap index')
    entries = ElementTree.fromstring(request(paths[0]))
    urls = {node.text for node in entries.findall('.//{*}loc')}
    for path in ('/', '/entities/', '/editorial/'):
        if SITE + path not in urls:
            raise ValueError(f'Missing sitemap entry for {path}')
    for path in ('/', '/editorial/', '/entities/codex-cli/', '/news/ollama-lm-studio-local-api/'):
        page = Page(markup=request(path))
        if page.canonical != SITE + path or page.noindex or (path != "/editorial/" and not page.schemas):
            raise ValueError(f'Unexpected public metadata for {path}')
    for agent in SEARCH_AGENTS:
        page = Page(markup=request('/news/ollama-lm-studio-local-api/', agent=agent))
        if page.canonical != SITE + '/news/ollama-lm-studio-local-api/' or page.noindex:
            raise ValueError(f'Unexpected simulated user-agent response for {agent}')
    ElementTree.fromstring(request('/rss.xml'))
    request('/geo-check-missing-route/', expected=404)


if __name__ == '__main__':
    probe()
