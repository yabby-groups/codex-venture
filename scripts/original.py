"""Discover, qualify and measure practices and stories in the existing queue."""
import http.client
import json
import os
import re
from pathlib import Path
from urllib.parse import urlencode

from collect import canonical, collect, digest, save
from community import hn_rows
from evidence import document, enrich, record

TYPES = {
    'practices': {'tutorials', 'workflows', 'prompts', 'comparisons'},
    'stories': {'stories', 'building-in-public', 'insights'},
}
PROJECT = 'https://github.com/yabby-groups/codex-venture'
API = 'https://api.github.com/repos/yabby-groups/codex-venture'
PUBLIC_PATHS = (
    'scripts/hosted.py', 'scripts/operations_queue.py', 'scripts/collect.py',
    'scripts/evidence.py', 'scripts/resource_ingest.py', 'scripts/check.py',
    '.github/workflows/venture.yml', 'astro.config.mjs', 'wrangler.jsonc',
)
WORK = Path(os.environ.get('RUNNER_TEMP', '.venture-runtime')) / 'venture'


def ready(section, item):
    documents = item.get('evidence') or []
    return (item['status'] == 'pending' and item.get('content_type') in TYPES[section]
            and (bool(item.get('discovery', {}).get('demand_id'))
                 or any(doc.get('excerpt') and not doc['label'].startswith('Community discussion')
                        for doc in documents)))


def issues(body):
    for row in json.loads(body)['items']:
        if len(row.get('body') or '') >= 400:
            yield (row['title'], row['html_url'], row['closed_at'] or row['created_at'],
                   row['body'], {'author': row['user']['login'], 'github_issue': row['url']})


def discover(section, now):
    slot = now.toordinal() % 3
    if section == 'stories':
        query = ('AI agent built', 'AI coding workflow', 'local LLM')[slot]
        sources = [
            dict(id=f'original-show-hn-{slot}', kind='discovery', category='coding', content_type='stories',
                 parse=hn_rows, interval_hours=12, url='https://hn.algolia.com/api/v1/search?' +
                 urlencode(dict(query=query, tags='show_hn', hitsPerPage=16))),
            dict(id='simon-willison', kind='feed', category='coding', content_type='stories', interval_hours=12,
                 url='https://simonwillison.net/atom/everything/'),
            dict(id='original-hamel', kind='feed', category='coding', content_type='stories', interval_hours=24,
                 url='https://hamel.dev/index.xml'),
            dict(id='original-github-issues', kind='discovery', category='agents', content_type='stories',
                 parse=issues, interval_hours=24, url='https://api.github.com/search/issues?' + urlencode(
                     dict(q='repo:openai/codex is:issue is:closed comments:>4', sort='updated', per_page=10))),
        ]
    else:
        sources = [
            dict(id='original-cloudflare-developers', kind='feed', category='coding', content_type='tutorials',
                 interval_hours=24, url='https://blog.cloudflare.com/tag/developers/rss/'),
            dict(id='original-huggingface-guides', kind='feed', category='open-source', content_type='tutorials',
                 interval_hours=24, url='https://huggingface.co/blog/feed.xml'),
        ]
    collect(14, sources, only_extra=True)


def operations(section, items, now):
    if os.getenv('VENTURE_PUBLIC_PROJECT') != 'true':
        return
    try:
        changes = json.loads(document(API + '/commits?sha=main&per_page=60'))
    except (OSError, ValueError, KeyError, TypeError, http.client.HTTPException) as error:
        print(f'Public commit discovery: {type(error).__name__}', flush=True)
        return
    try:
        runs = json.loads(document(API + '/actions/workflows/venture.yml/runs?per_page=20'))['workflow_runs']
    except (OSError, ValueError, KeyError, TypeError, http.client.HTTPException) as error:
        print(f'Public Actions discovery: {type(error).__name__}', flush=True)
        runs = []
    try:
        for change in changes:
            revision = change['sha']
            if not re.fullmatch(r'[a-f0-9]{40}', revision):
                continue
            entry = change['commit']
            subject = entry['message'].splitlines()[0]
            if (not re.search(r'collect|recover|budget|deploy|search|backlog|publish|index|cost|evidence|retry',
                              subject, re.I) or subject == 'Publish Codex Venture bilingual coverage'):
                continue
            kind = 'building-in-public' if re.search(r'recover|deploy|publish|failure', subject, re.I) else 'workflows'
            if kind not in TYPES[section]:
                continue
            url = PROJECT + '/commit/' + revision
            if digest(url) in items:
                continue
            detail = json.loads(document(API + '/commits/' + revision))
            files = [row for row in detail.get('files', []) if row['filename'] in PUBLIC_PATHS]
            if not files:
                continue
            run = next((row for row in runs if row['head_sha'] == revision
                        and row['head_branch'] == 'main' and row['event'] in ('schedule', 'workflow_dispatch')
                        and row['conclusion'] and type(row['id']) is int), None)
            docs = [record(url, 'Public production commit', subject + '\nChanged entry points: ' +
                           ', '.join(row['filename'] for row in files))]
            if run:
                docs.append(record(f"{PROJECT}/actions/runs/{run['id']}", 'Public Actions run',
                                   f"Trigger: {run['event']}. Conclusion: {run['conclusion']}. "
                                   "Workflow conclusion alone does not establish a specific fix or deployment."))
            add(items, url, subject, entry['committer']['date'], now, kind, 'public-operations', docs)
            # Continue next round from the existing, durable item IDs.
            return
    except (OSError, ValueError, KeyError, TypeError, http.client.HTTPException) as error:
        print(f'Public operations discovery: {type(error).__name__}', flush=True)


def add(items, url, title, published, now, kind, basis, docs, **extra):
    key = digest(canonical(url))
    if key in items:
        return
    items[key] = dict(url=canonical(url), published=published, discovered=now.isoformat(), source='original',
                      source_url=canonical(url), category='coding', title=title, summary=docs[0]['excerpt'],
                      fingerprint=digest(title + url), status='pending', content_type=kind,
                      basis=basis, evidence=docs, verified_at=now.isoformat(), **extra)


def prepare(section, items, now):
    operations(section, items, now)
    if section == 'practices' and os.getenv('VENTURE_EXPERIMENTS_ENABLED') == 'true':
        # This recipe uses the dependency already installed by the trusted lockfile.
        # A new version gets a new candidate. Other discovered tools are documentation leads.
        from practice_probe import UPSTREAM, run
        if digest(canonical(UPSTREAM)) not in items:
            receipt = run()
            add(items, UPSTREAM, 'Pagefind language detection on a bilingual fixture',
                now.isoformat(), now, 'tutorials', 'experiment',
                [record(UPSTREAM, 'Observed Pagefind probe and upstream version',
                        json.dumps(receipt, ensure_ascii=False))], experiment=receipt)
    pending = sorted((key for key, row in items.items() if row['status'] == 'pending'
                      and row.get('content_type') in TYPES[section] and not row.get('basis')),
                     key=lambda key: items[key]['published'], reverse=True)
    # Check new and recently published accounts first, then retry older sources.
    pending.sort(key=lambda key: (items[key].get('evidence_checked', ''),
                                  -items[key].get('discovery', {}).get('demand_priority', 0)))
    enrich(items, pending, now, limit=8)


def report(section, items, articles, receipt=None):
    published = [row['published'] for row in articles if row.get('type') in TYPES[section]]
    rows = [row for row in items.values() if row.get('content_type') in TYPES[section]]
    pending = sum(row['status'] == 'pending' for row in rows)
    evidenced = sum(ready(section, row) for row in rows)
    stats = dict(section=section, pending=pending, evidence_ready=evidenced,
                 needs_evidence=pending - evidenced, published=len(published),
                 latest_published=max(published, default=None), experiments={})
    for row in rows:
        if trial := row.get('experiment'):
            state = trial['status']
            stats['experiments'][state] = stats['experiments'].get(state, 0) + 1
    if receipt is not None:
        stats['model_usage'] = receipt.get('usage')
        stats['model_sessions'] = receipt.get('sessions', 0)
        stats['estimated_cost'] = [batch['estimated_cost'] for batch in receipt.get('batches', [])
                                   if batch.get('estimated_cost')] or None
        stats['billed_cost'] = receipt.get('billed_cost')
    save(WORK / (section + '.json'), stats)
    public = {key: value for key, value in stats.items()
              if key not in ('estimated_cost', 'billed_cost', 'model_usage', 'model_sessions')}
    print('Section queue:', json.dumps(public), flush=True)
