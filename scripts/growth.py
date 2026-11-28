"""Private demand, refresh and distribution records for the VPS operator."""
from datetime import date, timedelta
import re
from urllib.parse import urlencode

from collect import collect, digest, load, save, timestamp
from community import hn_rows
from original import issues


QUESTION = re.compile(r"\?|^(how|why|can|does|what|which|anyone|is there|looking for)\b", re.I)
HN_TOPIC = re.compile(r'\b(llms?|local models?|ollama|codex|chatgpt|claude|openrouter|ai|stable diffusion|comfyui)\b', re.I)
WEIGHTS = dict(demand=25, utility=20, click=15, novelty=15, search=10, longevity=10, sharing=5)


def question_rows(parser, topic=None):
    def parse(body):
        for title, url, published, summary, details in parser(body):
            if QUESTION.search(title) and (topic is None or topic.search(title)):
                yield title, url, published, summary, {**details, 'demand_question': title}
    return parse


def sources():
    github = urlencode(dict(q='repo:openai/codex is:issue is:open comments:>1', sort='updated', per_page=20))
    hn = [
        dict(id=provider, kind='discovery', category=category, content_type='tutorials',
             url='https://hn.algolia.com/api/v1/search_by_date?' +
             urlencode(dict(query=query, tags='ask_hn', hitsPerPage=20)),
             parse=question_rows(hn_rows, HN_TOPIC))
        for provider, query, category in (
            ('demand-hn', 'LLM', 'models'),
            ('demand-hn-chatgpt', 'ChatGPT', 'models'),
            ('demand-hn-ollama', 'Ollama', 'models'),
            ('demand-hn-creation', 'AI image', 'models'),
            ('demand-hn-automation', 'AI automation', 'agents'),
        )
    ]
    return hn + [
        dict(id='demand-github', kind='discovery', category='coding', content_type='tutorials',
             url='https://api.github.com/search/issues?' + github, parse=question_rows(issues)),
    ]


def tokens(title):
    return set(re.findall(r'[a-z0-9]+', title.casefold())) - {
        'how', 'can', 'what', 'does', 'the', 'with', 'you', 'use', 'for', 'to', 'my', 'a', 'in', 'i', 'ask', 'hn'
    }


def similar(left, right):
    return bool(left and right) and len(left & right) / len(left | right) >= 0.72


def discover(root, items_path, health_path, now):
    providers = sources()
    collect(30, providers, only_extra=True)
    health = load(health_path, {})
    items = load(items_path, {})
    path = root / 'opportunities.json'
    pool = load(path, {'version': 1, 'opportunities': {}})['opportunities']
    index = {lead: key for key, opportunity in pool.items() for lead in opportunity['evidence']}
    for item_id, item in sorted(items.items()):
        details = item.get('discovery', {})
        question = details.get('demand_question')
        if (not question or (item['source'].startswith('demand-hn') and not HN_TOPIC.search(question))
                or timestamp(item['published']) < now - timedelta(days=30)):
            continue
        url = details.get('discussion') or item['url']
        key = index.get(url) or next((
            key for key, candidate in pool.items() if similar(tokens(question), tokens(candidate['question']))
        ), digest(url))
        row = pool.setdefault(key, {'question': question, 'evidence': {},
                                    'first_seen': item['discovered']})
        row['evidence'][url] = {'item_id': item_id, 'published': item['published'],
                                'observed': item['discovered'], 'source': url.split('/')[2]}
        index[url] = key
    for item in items.values():
        details = item.get('discovery', {})
        details.pop('demand_id', None)
        details.pop('demand_priority', None)
    for key, row in list(pool.items()):
        if any(lead['source'] == 'news.ycombinator.com' for lead in row['evidence'].values()) and not HN_TOPIC.search(row['question']):
            del pool[key]
            continue
        evidence = list(row['evidence'].values())
        active = [lead for lead in evidence if timestamp(lead['published']) >= now - timedelta(days=30)]
        coverage = sorted({route for lead in evidence
                           for route in items.get(lead['item_id'], {}).get('articles', [])})
        week = sum(timestamp(lead['published']) >= now - timedelta(days=7) for lead in active)
        prior = sum(now - timedelta(days=14) <= timestamp(lead['published']) < now - timedelta(days=7)
                    for lead in active)
        domains = len({lead['source'] for lead in active})
        score = dict.fromkeys(WEIGHTS)
        score['demand'] = min(WEIGHTS['demand'], len(active) * 4 + domains * 3)
        score['search'] = None
        row.update(last_seen=max(lead['observed'] for lead in evidence), independent_source_domains=domains,
                   recent_discussions=week, prior_discussions=prior, trend_delta=week - prior,
                   audience='AI tool users and developers', demand_type='public question',
                   intent='problem solving', covered_routes=coverage, score=score,
                   measured_score=sum(value for value in score.values() if value is not None),
                   research_difficulty='unknown', evidence_completeness='community_leads',
                   status='covered' if coverage else 'research' if active else 'expired')
        if not active and timestamp(row['last_seen']) < now - timedelta(days=90):
            del pool[key]
    statuses = {}
    for provider in providers:
        key = provider['id']
        entry = health.get(key, {})
        statuses[key] = dict(status='unavailable' if entry.get('failures') else
                             'available' if entry.get('last_success') else 'unknown',
                             last_success=entry.get('last_success'), reason=entry.get('error'),
                             retry_after=entry.get('retry_after'), budget_pause=entry.get('budget_pause'))
    save(path, dict(version=1, scanned_at=now.isoformat(), sources=statuses, opportunities=pool))
    for key, candidate in pool.items():
        if candidate['status'] != 'research':
            continue
        for lead in candidate['evidence'].values():
            item = items.get(lead['item_id'])
            if item and timestamp(item['published']) >= now - timedelta(days=30):
                item['discovery'].update(demand_id=key, demand_priority=candidate['measured_score'])
    save(items_path, items)
    return {'demand_research': sum(row['status'] == 'research' for row in pool.values()),
            'providers': {key: row['status'] for key, row in statuses.items()}}


def daily(root, analytics, stamp, articles):
    from analytics import content, report
    end = date.fromisoformat(stamp)
    inventory = content(articles)
    windows = {days: report(analytics, end - timedelta(days=days - 1), end, inventory)
               for days in (1, 7, 28)}
    refresh = [dict(row, reason='low search CTR', status='research')
               for row in windows[28]['google_pages']
               if row['impressions'] >= 100 and row['clicks'] / row['impressions'] < 0.02]
    demand = load(root / 'opportunities.json', {})
    opportunities = sorted(demand.get('opportunities', {}).items(),
                           key=lambda pair: pair[1]['measured_score'], reverse=True)
    save(root / 'reports' / (stamp + '.json'), {
        'version': 1, 'facts': {'windows': windows, 'demand_sources': demand.get('sources', {}),
                               'distribution_drafts': len(list((root / 'distribution').glob('*.json')))
                               if (root / 'distribution').exists() else None},
        'inferences': {'refresh_candidates': refresh},
        'hypotheses': {'demand': [dict(row, id=key) for key, row in opportunities
                                  if row['status'] == 'research'][:12]},
        'executed': ['read provider snapshots', 'search CTR scan'],
        'planned': ['review source evidence for leading opportunities'],
        'blocked': ['automatic social distribution requires channel authorization'],
    })
    return {'refresh_candidates': len(refresh)}


def distribution(root, routes, articles, sha):
    route_set = {'/' + route.strip('/') + '/' for route in routes}
    count = 0
    for article in articles:
        route = f"/{article['collection']}/{article['slug']}/"
        if route not in route_set:
            continue
        title, summary = article.get('titleEn'), article.get('summaryEn')
        if not (title and summary):
            continue
        revision = digest(route + '\n' + title + '\n' + summary)
        path = root / 'distribution' / (revision + '.json')
        if path.exists():
            continue
        def link(channel):
            return 'https://codex-venture.com' + route + '?' + urlencode(
                dict(utm_source=channel, utm_medium='social', utm_campaign='editorial'))
        save(path, {'version': 1, 'sha': sha, 'route': route, 'variants': {
            'x': {'status': 'draft_only', 'text': title[:180] + '\n' + link('x')},
            'bluesky': {'status': 'draft_only', 'text': summary[:170].rsplit(' ', 1)[0] + '\n' + link('bluesky')},
            'hacker_news': {'status': 'requires_approval', 'title': title, 'url': link('hacker_news')},
            'dev': {'status': 'disabled', 'reason': 'Requires standalone article and canonical review'},
            'reddit': {'status': 'requires_approval', 'reason': 'Requires subreddit rule review'},
            'github': {'status': 'disabled', 'reason': 'Requires a reusable project artifact'},
        }})
        count += 1
    return count


def relevant_coverage(articles, candidates):
    """Keep exact source matches and a small set of title matches."""
    urls = {candidate.get('url') for candidate in candidates.values()}
    urls.update(doc['url'] for candidate in candidates.values() for doc in candidate.get('documents', []))
    titles = [tokens(candidate.get('title', '')) for candidate in candidates.values()]
    ranked = []
    for index, article in enumerate(articles):
        exact = any(source['url'] in urls for source in article.get('sources', []))
        words = tokens(article.get('titleEn', ''))
        overlap = max((len(words & title) for title in titles), default=0)
        if exact or overlap >= 2:
            ranked.append((not exact, -overlap, index, article))
    return [row[3] for row in sorted(ranked)[:12]]
