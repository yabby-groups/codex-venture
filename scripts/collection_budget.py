"""Persist local ceilings and provider backoff across hosted runs."""

import os
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

PATH = Path('.venture-runtime/requests.json')
LIMITS = {
    'api.github.com': (240, 1400),
    'github.com': (20, 100),
    'public.api.bsky.app': (40, 200),
    'huggingface.co': (75, 300),
    'hn.algolia.com': (40, 200),
    'hacker-news.firebaseio.com': (40, 200),
    'dev.to': (20, 100),
}


class CollectionPaused(OSError):
    def __init__(self, host, reason, resume):
        self.host = host
        self.reason = reason
        self.resume = resume
        super().__init__(f'{host}: {reason}')


def reserve(host):
    from collect import load, save

    now = datetime.now(timezone.utc)
    state = load(PATH, {})
    day = now.date().isoformat()
    hour = now.strftime('%Y-%m-%dT%H')
    if day != state.get('day'):
        state = {'day': day, 'providers': {
            name: {'resume': row['resume']} for name, row in state.get('providers', {}).items()
            if row.get('resume', 0) > now.timestamp()
        }}
    row = state['providers'].setdefault(host, {})
    if row.get('hour') != hour:
        row.update(hour=hour, hourly=0)
    hourly, daily = LIMITS.get(host, (24, 100))
    if row.get('resume', 0) > now.timestamp():
        raise CollectionPaused(host, 'provider rate limit', row['resume'])
    resource = os.getenv('VENTURE_COLLECTION_LANE') == 'resource'
    hourly_limit = hourly * 2 // 3 if resource else hourly
    daily_limit = daily * 2 // 3 if resource else daily
    if row.get('daily', 0) >= daily_limit:
        raise CollectionPaused(host, 'local daily request allowance', (int(now.timestamp()) // 86400 + 1) * 86400)
    if row.get('hourly', 0) >= hourly_limit:
        raise CollectionPaused(host, 'local hourly request allowance', (int(now.timestamp()) // 3600 + 1) * 3600)
    row['hourly'] += 1
    row['daily'] = row.get('daily', 0) + 1
    save(PATH, state)


def record(host, status, headers):
    from collect import load, save

    state = load(PATH, {})
    row = state['providers'][host]
    remaining = headers.get('X-RateLimit-Remaining')
    reset = headers.get('X-RateLimit-Reset')
    retry = headers.get('Retry-After')
    now = datetime.now(timezone.utc).timestamp()
    row['responses'] = row.get('responses', 0) + 1
    if status < 300 or status == 304:
        row['successes'] = row.get('successes', 0) + 1
    if remaining and remaining.isdigit():
        row['remaining'] = int(remaining)
    if status == 429 or remaining == '0' or (status in (403, 503) and retry):
        row['limited'] = row.get('limited', 0) + 1
        resume = float(reset) if reset and reset.isdigit() and remaining == '0' else now + 900
        if retry:
            try:
                until = now + int(retry) if retry.isdigit() else parsedate_to_datetime(retry).timestamp()
                resume = max(resume, until)
            except (TypeError, ValueError, OverflowError):
                pass
        row['resume'] = max(row.get('resume', 0), resume)
    save(PATH, state)
