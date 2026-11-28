"""Private daily snapshots and reproducible period reports."""
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from decimal import Decimal
import os
from pathlib import Path
import re
import sys
from statistics import median
from urllib.parse import urlsplit

from analytics_sources import bing, cloudflare, google, myna_billing
from collect import canonical, load, save
from commerce_analytics import adsense, affiliate, edge, exported_requests, ga4, google_token
from editor import DATE_ZONE, metadata
from geo import bing_citation_export, referral_totals

SITE = 'https://codex-venture.com'
ALIASES = load(Path('config/article-aliases.json'), {})


def route(value):
    url = urlsplit(value)
    if url.netloc and url.hostname != 'codex-venture.com':
        return None
    path = '/' + url.path.strip('/') + '/'
    return ALIASES.get(path, path)


def github_project(value):
    url = urlsplit(value)
    parts = url.path.strip('/').split('/')
    if url.hostname != 'github.com' or len(parts) < 2 or parts[0] in {
        'topics', 'orgs', 'users', 'search', 'trending', 'marketplace', 'collections', 'sponsors',
    }:
        return None
    return '/'.join(parts[:2]).lower()


def content(articles):
    inventory = {}
    sources, projects = set(), set()
    kinds, categories, days, weeks, months = (Counter() for _ in range(5))
    news_sources = []
    for article in articles:
        path = f"/{article['collection']}/{article['slug']}/"
        day = datetime.fromisoformat(article['published']).astimezone(DATE_ZONE).date()
        urls = {canonical(source['url']) for source in article['sources']}
        domains = {urlsplit(url).hostname for url in urls}
        repos = {project for url in urls if (project := github_project(url))}
        news = article['collection'] == 'news'
        category = article['category']
        kind = ('news' if news else 'weekly' if article['slug'].startswith('weekly-') else 'daily')
        kinds[kind] += 1
        if news:
            news_sources.extend(urls)
            if category == 'open-source' and repos:
                kinds['github_recommendations'] += 1
            if category == 'models':
                kinds['model_news'] += 1
        categories[category] += 1
        days[day.isoformat()] += 1
        weeks[(day - timedelta(days=day.weekday())).isoformat()] += 1
        months[day.isoformat()[:7]] += 1
        sources.update(domains)
        projects.update(repos)
        inventory[path] = {'category': category, 'kind': kind, 'date': day.isoformat(),
                           'sources': sorted(domains), 'projects': sorted(repos)}
        if article.get('editorial'):
            inventory[path]['editorial'] = article['editorial']
    return dict(total=len(articles), kinds=kinds, categories=categories, sources=len(sources),
                unique_github_projects=len(projects), days=days, weeks=weeks, months=months,
                source_coverage=sum(bool(a['sources']) for a in articles) / len(articles) if articles else None,
                news_source_duplicate_rate=(len(news_sources) - len(set(news_sources))) / len(news_sources)
                if news_sources else None, inventory=inventory)


def period(task, today):
    end = today - timedelta(days=1)
    if task == 'weekly':
        end = today - timedelta(days=today.weekday() + 1)
        return end - timedelta(days=6), end
    if task == 'monthly':
        end = today.replace(day=1) - timedelta(days=1)
        return end.replace(day=1), end
    return end, end


def days_between(start, end):
    return ((start + timedelta(days=i)).isoformat() for i in range((end - start).days + 1))


def enabled_data(snapshot, key):
    item = snapshot.get('metrics', {}).get(key, {})
    return item.get('data') if item.get('status') == 'available' else None


def reader_performance(paths, commercial, clicks, impressions):
    observed = Counter()
    by_path = defaultdict(Counter)
    content_events = {'article_copy', 'related_article_click'} | {
        f'article_depth_{level}' for level in (25, 50, 75, 100)
    }
    for day in commercial.values():
        snapshot = day['ga4']
        if not isinstance(snapshot, dict):
            continue
        for metric in ('pages', 'content_events', 'recommendations'):
            result = enabled_data(snapshot, metric)
            if result is None:
                continue
            observed[metric] += 1
            for row in result.get('rows', []):
                if 'dimensionValues' not in row:
                    continue
                dimensions = [value['value'] for value in row['dimensionValues']]
                values = [value['value'] for value in row['metricValues']]
                if metric == 'pages':
                    path = route(dimensions[0])
                    if path in paths:
                        views, seconds, _ = values
                        by_path[path].update(views=int(views), engagement_seconds=float(seconds))
                else:
                    event, value = dimensions
                    allowed = content_events if metric == 'content_events' else {'editorial_impression', 'editorial_click'}
                    path = route(value)
                    if event in allowed and path in paths:
                        by_path[path][event] += int(values[0])
    articles = {}
    for path, article in paths.items():
        if 'editorial' not in article:
            continue
        counts = by_path.get(path, {})
        views = counts.get('views')
        exposed = counts.get('editorial_impression', 0)
        articles[path] = {
            'editorial': article['editorial'],
            'ga4_reported': dict(counts),
            'sample': ('unavailable' if not observed['pages'] else 'no_reported_views' if not views
                       else 'insufficient' if views < 100 else 'observed'),
            'engagement_seconds_per_view': counts['engagement_seconds'] / views if views else None,
            'recommendation_clicks_per_impression': counts.get('editorial_click', 0) / exposed if exposed and counts.get('editorial_click') is not None else None,
            'search_clicks': clicks.get(path) if path in impressions else None,
            'search_impressions': impressions.get(path),
        }
    return {'observed_days': dict(observed), 'articles': articles,
            'scope': 'Reported consented GA4 rows, subject to row limits and privacy thresholds'}



def report(root, start, end, stats):
    dates = list(days_between(start, end))
    paths = stats['inventory']
    views, categories = Counter(), Counter()
    clicks, impressions = Counter(), Counter()
    keyword_clicks, keyword_impressions = Counter(), Counter()
    source_yield = Counter(source for article in paths.values() if article['date'] in dates
                           for source in article['sources'])
    provider_days = Counter()
    ai_referrals = Counter()
    referral_days = 0
    all_referrals = Counter()
    commercial = {}
    totals = defaultdict(dict)
    for day in dates:
        commercial[day] = commercial_day(root, day)
        traffic = load(root / 'traffic' / (day + '.json'), {})
        search = load(root / 'search' / 'google' / (day + '.json'), {})
        for provider, snapshot in [('cloudflare', traffic), ('google', search)]:
            if snapshot.get('status') == 'available':
                provider_days[provider] += 1
        for key in ('page_views', 'visits'):
            rows = enabled_data(traffic, key)
            if rows:
                totals[day][key] = rows[0].get('count', rows[0].get('sum', {}).get('pageViews')) if key == 'page_views' else rows[0]['sum'].get('visits')
        referrals = enabled_data(traffic, 'referrers')
        if referrals is not None:
            ai_referrals.update(referral_totals(referrals))
            for row in referrals:
                host = row['dimensions'].get('refererHost') or '(direct / unknown)'
                all_referrals[host] += row['count']
            referral_days += 1
        search_totals = enabled_data(search, 'totals')
        if search_totals and search_totals['rows']:
            totals[day]['google'] = {key: search_totals['rows'][0].get(key)
                                    for key in ('clicks', 'impressions', 'ctr', 'position')}
        for row in enabled_data(traffic, 'pages') or []:
            path = route(row['dimensions']['requestPath'])
            if path in paths:
                count = row.get('count', row.get('sum', {}).get('pageViews'))
                views[path] += count
                categories[paths[path]['category']] += count
        for row in (enabled_data(search, 'page') or {}).get('rows', []):
            path = route(row['keys'][0])
            if path in paths:
                clicks[path] += row['clicks']
                impressions[path] += row['impressions']
        for row in (enabled_data(search, 'query') or {}).get('rows', []):
            keyword = row['keys'][0]
            keyword_clicks[keyword] += row['clicks']
            keyword_impressions[keyword] += row['impressions']
    latest_search = next(({
        'date': previous.isoformat(),
        'metrics': snapshot['metrics'],
        'timezone': 'America/Los_Angeles',
    } for previous in (end - timedelta(days=offset) for offset in range(8))
        if (snapshot := load(root / 'search/google' / (previous.isoformat() + '.json'), {}))
        .get('status') == 'available'), 'UNKNOWN')
    next_topics = [
        {'path': path, 'views': count, 'category': paths[path]['category']}
        for path, count in views.most_common(20)
    ]
    strategy = {
        'preferred_formats': ['original-practice', 'deployment-tutorial', 'hands-on-review', 'product-comparison'],
        'audience_evidence': next_topics[:5] or 'UNKNOWN',
        'search_evidence_day': latest_search['date'] if isinstance(latest_search, dict) else 'UNKNOWN',
        'action': ('Plan a documented follow-up for the strongest observed topics.'
                   if next_topics else 'Preserve current topic weights until article traffic is available.'),
    }
    projects = Counter()
    for path, count in views.items():
        for project in paths[path]['projects']:
            projects[project] += count
    bing_snapshots = [day for day in dates
                      if load(root / 'search/bing' / (day + '.json'), {}).get('status') == 'available']
    if bing_snapshots:
        provider_days['bing_snapshots'] = len(bing_snapshots)
    runs = [load(file, {}) for day in dates for file in (root / 'operations' / day).glob('*.json')]
    costs = defaultdict(Decimal)
    models = defaultdict(lambda: Counter())
    observed = Counter()
    unknown = 0
    for run in runs:
        receipt = run.get('model')
        if not receipt:
            continue
        usage = receipt.get('usage') or {}
        observed.update(usage)
        name = receipt.get('model') or 'unknown'
        models[name]['sessions'] += receipt.get('sessions', 0)
        models[name][receipt['status']] += 1
        models[name].update(usage)
        price = receipt.get('estimated_cost')
        if price is None:
            unknown += 1
        else:
            costs[price['currency']] += Decimal(price['amount'])
            models[name]['cost_' + price['currency']] += Decimal(price['amount'])
    billed = [load(root / 'costs' / 'myna' / (day + '.json'), {}) for day in dates]
    billed = [snapshot['data'] for snapshot in billed if snapshot.get('status') == 'available']
    billed_by_model = defaultdict(Decimal)
    for snapshot in billed:
        for model, amount in snapshot['by_model'].items():
            billed_by_model[model] += Decimal(amount)
    published = sum(run.get('published', 0) for run in runs)
    citation_data = bing_citation_export(root / 'geo' / 'bing' / f'{start}_{end}.csv')
    return dict(start=start.isoformat(), end=end.isoformat(), expected_days=len(dates),
                geo={'referrer_pageviews': dict(ai_referrals), 'referrer_observed_days': referral_days,
                     'referrer_scope': 'Cloudflare RUM top 100 reported hosts per day (UTC)',
                     'verified_crawler_logs': 'UNKNOWN', 'bing_ai_citations': citation_data,
                     'google_ai_performance': 'UNKNOWN'},
                observed_days=provider_days, daily_metrics=totals,
                browser_visits={day: totals[day].get('visits', 'UNKNOWN') for day in dates},
                referrer_pageviews=dict(all_referrals.most_common(30)) if referral_days else 'UNKNOWN',
                latest_final_search=latest_search, monetization=commercial, next_content=strategy,
                reader_performance=reader_performance(paths, commercial, clicks, impressions),
                new_articles={d: stats['days'].get(d, 0) for d in dates},
                top_articles=[{'path': path, 'views': count, **paths[path]}
                              for path, count in views.most_common(20)],
                category_views=categories,
                project_article_views=dict(projects.most_common(20)),
                sources_by_article_yield=dict(source_yield.most_common(20)),
                latest_bing_rolling_snapshot=bing_snapshots[-1] if bing_snapshots else None,
                google_queries=[dict(query=key, clicks=count, impressions=keyword_impressions[key])
                                for key, count in keyword_clicks.most_common(20)],
                google_pages=[dict(path=path, clicks=clicks[path], impressions=count,
                                   ctr=clicks[path] / count if count else None)
                              for path, count in impressions.most_common(20)],
                sessions_by_model={name: {key: str(value) if isinstance(value, Decimal) else value
                                         for key, value in model.items()} for name, model in models.items()}, observed_tokens=observed, operations=len(runs),
                operation_tasks=Counter(run.get('task') for run in runs),
                published=published, sessions_without_estimate=unknown,
                billed_cost={'currency': 'USD', 'amount': str(sum(Decimal(s['amount']) for s in billed)),
                             'observed_days': len(billed),
                             'by_model': {name: str(amount) for name, amount in billed_by_model.items()}}
                if billed else None,
                known_estimated_cost={key: str(value) for key, value in costs.items()},
                estimated_cost_per_published_article={key: str(value / published) for key, value in costs.items()}
                if published and not unknown else None)


def commercial_day(root, day):
    def evidence(snapshot):
        return snapshot if snapshot.get('status') == 'available' else 'UNKNOWN'

    current = load(root / 'commerce/edge' / (day + '.json'), {})
    hourly = enabled_data(current, 'hourly')
    history = []
    for previous in (date.fromisoformat(day) - timedelta(days=n) for n in range(1, 8)):
        snapshot = load(root / 'commerce/edge' / (previous.isoformat() + '.json'), {})
        values = (enabled_data(snapshot, 'hourly') or {}).get('rows', [])
        if values:
            history.append(max(row['count'] for row in values))
    peak = 'UNKNOWN'
    if hourly and hourly['rows']:
        row = max(hourly['rows'], key=lambda item: item['count'])
        baseline = median(history) if len(history) >= 3 else None
        peak = {'hour': row['dimensions']['datetimeHour'], 'requests': row['count'],
                'baseline_days': len(history), 'median_daily_peak': baseline,
                'above_3x_baseline': row['count'] >= 3 * baseline if baseline else 'UNKNOWN'}
    return {
        'peak_diagnostic': peak,
        'ga4': evidence(load(root / 'commerce/ga4' / (day + '.json'), {})),
        'adsense': evidence(load(root / 'commerce/adsense' / (day + '.json'), {})),
        'edge_requests': evidence(current),
        'request_classification': evidence(exported_requests(root / 'imports/requests' / (day + '.ndjson'))),
        'affiliate': evidence(affiliate(root / 'imports/affiliate' / (day + '.json'))),
    }


def sync_commerce(root, days):
    providers = {}
    for day in days:
        for name, adapter in [('ga4', ga4), ('adsense', adsense), ('edge', edge)]:
            snapshot = adapter(day)
            path = root / 'commerce' / name / (day + '.json')
            if snapshot['status'] == 'available' or not path.exists():
                save(path, snapshot)
            providers[name] = snapshot['status']
    return providers


def operator_daily(root, articles):
    day = datetime.now(timezone.utc).date() - timedelta(days=1)
    # Keep the reporting window stable across retries and provider timezones.
    snapshot = cloudflare(day.isoformat())
    path = root / 'traffic' / (day.isoformat() + '.json')
    if snapshot['status'] == 'available' or not path.exists():
        save(path, snapshot)
    sync_commerce(root, days_between(day - timedelta(days=2), day))
    if os.getenv('GOOGLE_SEARCH_CONSOLE_PROPERTY'):
        search_day = datetime.now(ZoneInfo('America/Los_Angeles')).date() - timedelta(days=3)
        from analytics_sources import result
        token = result(lambda: google_token('GOOGLE_SEARCH')).get('data')
        if token:
            os.environ['GOOGLE_ACCESS_TOKEN'] = token
        snapshot = google(search_day.isoformat())
        path = root / 'search/google' / (search_day.isoformat() + '.json')
        if snapshot['status'] == 'available' or not path.exists():
            save(path, snapshot)
    bing_path = root / 'search/bing' / (day.isoformat() + '.json')
    bing_snapshot = bing()
    if bing_snapshot['status'] == 'available' or not bing_path.exists():
        save(bing_path, bing_snapshot)
    articles = content(articles)
    save(root / 'reports/daily' / (day.isoformat() + '.json'), report(root, day, day, articles))
    return {'analytics_day': day.isoformat()}


def store():
    location = os.getenv('ANALYTICS_STORE')
    if location and (Path(location) / '.git').is_dir():
        return Path(location) / 'analytics'
    return None


def sync(root, task, today, lookback):
    providers = {}
    if task in ('all', 'traffic'):
        latest = datetime.now(timezone.utc).date() - timedelta(days=1)
        for day in days_between(latest - timedelta(days=lookback - 1), latest):
            snapshot = cloudflare(day)
            path = root / 'traffic' / (day + '.json')
            if snapshot['status'] == 'available' or not path.exists():
                save(path, snapshot)
            providers['Cloudflare RUM'] = snapshot['status']
        providers.update(sync_commerce(root, days_between(latest - timedelta(days=min(lookback, 3) - 1), latest)))
    if task in ('all', 'search'):
        search_day = datetime.now(ZoneInfo('America/Los_Angeles')).date()
        end = search_day - timedelta(days=3)
        urls = [SITE + route(f"/{a['collection']}/{a['slug']}/") for a in metadata()[:2]]
        for day in days_between(end - timedelta(days=lookback - 1), end):
            snapshot = google(day, urls if day == end.isoformat() else ())
            save(root / 'search/google' / (day + '.json'), snapshot)
            providers['Google Search Console'] = snapshot['status']
        snapshot = bing()
        save(root / 'search/bing' / (today.isoformat() + '.json'), snapshot)
        providers['Bing Webmaster Tools'] = snapshot['status']
    if task in ('all', 'search'):
        for day in days_between(today - timedelta(days=lookback), today - timedelta(days=1)):
            snapshot = myna_billing(date.fromisoformat(day), DATE_ZONE)
            path = root / 'costs' / 'myna' / (day + '.json')
            if snapshot['status'] == 'available' or not path.exists():
                save(path, snapshot)
            providers['Myna billing'] = snapshot['status']
    summary = os.getenv('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a') as output:
            output.write('| Provider | Latest sync status |\n| --- | --- |\n')
            for provider, status in providers.items():
                output.write(f'| {provider} | {status} |\n')


def main(task, domain='all', lookback='7'):
    root = store()
    if root is None:
        print('Analytics skipped because private storage is disabled.')
        return
    today = datetime.now(DATE_ZONE).date()
    if task == 'sync':
        sync(root, domain, today, min(30, max(1, int(lookback))))
        return
    stats = content(metadata())
    save(root / 'content' / (today.isoformat() + '.json'), stats)
    start, end = period(task, today)
    if os.getenv('GOOGLE_GA4_PROPERTY_ID'):
        for day in days_between(max(start, end - timedelta(days=2)), end):
            snapshot = ga4(day)
            path = root / 'commerce/ga4' / (day + '.json')
            if snapshot['status'] == 'available' or not path.exists():
                save(path, snapshot)
    data = report(root, start, end, stats)
    save(root / 'reports' / task / (end.isoformat() + '.json'), data)
    summary = os.getenv('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a') as output:
            output.write(f'| Public content | Count |\n| --- | ---: |\n| Published articles | {stats["total"]} |\n'
                         f'| New articles in period | {sum(data["new_articles"].values())} |\n')


if __name__ == '__main__':
    main(*sys.argv[1:])
