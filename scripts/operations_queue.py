"""Recover scheduled work from durable due times."""
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

from collect import load, save
from editor import DATE_ZONE

PATH = Path('.venture-runtime/operations.json')
INTERVALS = {
    'collect': 2, 'discover': 6, 'news': 2, 'resource-sync': 2,
    'daily': 24, 'weekly': 168, 'backfill': 24, 'resource-refresh': 168,
}


def select(request):
    now = datetime.now(DATE_ZONE)
    queue = load(PATH, {})
    if request == 'cycle':
        due = [task for task in INTERVALS if not queue.get(task, {}).get('due')
               or datetime.fromisoformat(queue[task]['due']) <= now]
        due = [task for task in due if task not in ('daily', 'weekly')
               or now.hour >= 20 and (task != 'weekly' or now.weekday() == 6)]
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
    if task in ('daily', 'weekly') and interval > 1:
        due = due.replace(hour=20, minute=0, second=0, microsecond=0)
    row.update(result=result, due=due.isoformat())
    if task == 'backfill' and result in ('PUBLISHED', 'NO_NEW_CONTENT'):
        row['window'] = (row.get('window', 0) + 1) % 3
    save(PATH, queue)
    message = json.dumps({'task': task, 'result': result, 'next_due': row['due']})
    print(message, flush=True)
    if summary := os.getenv('GITHUB_STEP_SUMMARY'):
        with open(summary, 'a') as output:
            output.write(f'- `{task}` → **{result}**\n')
