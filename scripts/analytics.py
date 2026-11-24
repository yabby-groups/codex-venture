"""Private daily snapshots and reproducible period reports."""
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from decimal import Decimal
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

from analytics_sources import bing, cloudflare, google
from collect import canonical, load, save
from editor import DATE_ZONE, metadata

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
    return dict(total=len(articles), kinds=kinds, categories=categories, sources=len(sources),
                unique_github_projects=len(projects), days=days, weeks=weeks, months=months,
                source_coverage=sum(bool(a['sources']) for a in articles) / len(articles) if articles else None,
                news_source_duplicate_rate=(len(news_sources) - len(set(news_sources))) / len(news_sources)
                if news_sources else None, inventory=inventory)


def period(task, today):
    end = today if task == 'daily' else today - timedelta(days=1)
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


def report(root, start, end, stats):
    dates = list(days_between(start, end))
    paths = stats['inventory']
    views, categories = Counter(), Counter()
    clicks, impressions = Counter(), Counter()
    keyword_clicks, keyword_impressions = Counter(), Counter()
    source_yield = Counter(source for article in paths.values() if article['date'] in dates
                           for source in article['sources'])
    provider_days = Counter()
    totals = defaultdict(dict)
    for day in dates:
        traffic = load(root / 'traffic' / (day + '.json'), {})
        search = load(root / 'search' / 'google' / (day + '.json'), {})
        for provider, snapshot in [('cloudflare', traffic), ('google', search)]:
            if snapshot.get('status') == 'available':
                provider_days[provider] += 1
        for key in ('page_views', 'visits'):
            rows = enabled_data(traffic, key)
            if rows:
                totals[day][key] = rows[0].get('count', rows[0].get('sum', {}).get('pageViews')) if key == 'page_views' else rows[0]['sum'].get('visits')
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
    published = sum(run.get('published', 0) for run in runs)
    return dict(start=start.isoformat(), end=end.isoformat(), expected_days=len(dates),
                observed_days=provider_days, daily_metrics=totals,
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
                published=published, sessions_without_estimate=unknown, billed_cost=None,
                known_estimated_cost={key: str(value) for key, value in costs.items()},
                estimated_cost_per_published_article={key: str(value / published) for key, value in costs.items()}
                if published and not unknown else None)


def store():
    location = os.getenv('ANALYTICS_STORE')
    if location and (Path(location) / '.git').is_dir():
        return Path(location) / 'analytics'
    return None


def sync(root, task, today, lookback):
    providers = {}
    if task in ('all', 'traffic'):
        for day in days_between(today - timedelta(days=lookback), today - timedelta(days=1)):
            snapshot = cloudflare(day)
            save(root / 'traffic' / (day + '.json'), snapshot)
            providers['Cloudflare RUM'] = snapshot['status']
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
    data = report(root, start, end, stats)
    save(root / 'reports' / task / (end.isoformat() + '.json'), data)
    summary = os.getenv('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a') as output:
            output.write(f'| Public content | Count |\n| --- | ---: |\n| Published articles | {stats["total"]} |\n'
                         f'| New articles in period | {sum(data["new_articles"].values())} |\n')


if __name__ == '__main__':
    main(*sys.argv[1:])
