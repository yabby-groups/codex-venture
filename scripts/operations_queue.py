"""Recover scheduled work from durable due times."""
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import Request, urlopen

from collect import load, save
from editor import DATE_ZONE
from release import PROBE_HEADERS

PATH = Path('.venture-runtime/operations.json')
INTERVALS = {
    'collect': 2, 'discover': 6, 'news': 2, 'resource-sync': 2,
    'daily': 24, 'weekly': 168, 'backfill': 24, 'resource-refresh': 168,
}


def public_coverage():
    request = Request('https://codex-venture.com/coverage.json', headers=PROBE_HEADERS)
    try:
        with urlopen(request, timeout=8) as response:
            return json.load(response)
    except (OSError, ValueError) as error:
        print(f'Public coverage unavailable: {error}', flush=True)
        return {}


def select(request):
    now = datetime.now(DATE_ZONE)
    queue = load(PATH, {})
    if request == 'cycle':
        due = [task for task in INTERVALS if not queue.get(task, {}).get('due')
               or datetime.fromisoformat(queue[task]['due']) <= now]
        due = [task for task in due if task not in ('daily', 'weekly')
               or now.hour >= 20 and (task != 'weekly' or now.weekday() == 6)
               or bool(queue.get(task, {}).get('due'))]
        if not due:
            return 'idle', 7
        request = min(due, key=lambda task: queue.get(task, {}).get('started', ''))
    row = queue.get(request, {})
    windows = (7, 30, 90)
    days = int(os.getenv('BACKFILL_DAYS') or windows[row.get('window', 0)])
    queue[request] = {**row, 'started': now.isoformat(), 'result': 'SKIPPED',
                      'due': (now + timedelta(minutes=30)).isoformat()}
    save(PATH, queue)
    return request, days


def record(task, result):
    queue = load(PATH, {})
    now = datetime.now(DATE_ZONE)
    row = queue.setdefault(task, {})
    interval = INTERVALS.get(task, 24)
    if result in ('BUDGET_BLOCKED', 'SOURCE_BLOCKED', 'DEPLOY_FAILED', 'BACKLOG', 'SKIPPED'):
        interval = 1
    due = now + timedelta(hours=interval)
    if interval > 1 and task == 'daily':
        due = (now + timedelta(days=1)).replace(hour=20, minute=0, second=0, microsecond=0)
    if interval > 1 and task == 'weekly':
        due = (now + timedelta(days=7 - (now.weekday() + 1) % 7)).replace(
            hour=20, minute=0, second=0, microsecond=0)
    row.update(result=result, due=due.isoformat())
    if task == 'backfill' and result in ('PUBLISHED', 'NO_NEW_CONTENT'):
        row['window'] = (row.get('window', 0) + 1) % 3
    dry = ('NO_NEW_CONTENT', 'BACKLOG', 'SOURCE_BLOCKED')
    if task != 'idle':
        row['consecutive_dry_runs'] = row.get('consecutive_dry_runs', 0) + 1 if result in dry else 0
    if task in ('news', 'backfill') and row.get('consecutive_dry_runs') == 2:
        discovery = queue.setdefault('discover', {})
        discovery['due'] = now.isoformat()
        print(f'{task} has produced no content twice ({result}); discovery requested', flush=True)
    save(PATH, queue)
    message = json.dumps({'task': task, 'result': result, 'next_due': row['due']})
    print(message, flush=True)
    if summary := os.getenv('GITHUB_STEP_SUMMARY'):
        with open(summary, 'a') as output:
            output.write(f'- `{task}` → **{result}**\n')
