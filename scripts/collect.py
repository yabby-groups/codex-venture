import hashlib
import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from functools import lru_cache
from html import unescape
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from pathlib import Path

AGENT = 'CodexVentureBot'
CATEGORIES = {'models', 'coding', 'image', 'video', 'audio', 'agents', 'open-source'}


def load(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n')
    temporary.replace(path)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def canonical(url):
    parts = urlsplit(url)
    if (parts.scheme != 'https' or not parts.hostname or parts.username or parts.password
            or re.search(r'[\\<>"\s\x00-\x1f]', url)):
        raise ValueError('expected a public HTTPS URL')
    query = sorted((key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True)
                   if not key.lower().startswith('utm_') and key.lower() not in {'fbclid', 'gclid'})
    return urlunsplit(('https', parts.netloc.lower(), parts.path.rstrip('/') or '/', urlencode(query), ''))


def clean(value):
    return ' '.join(unescape(re.sub(r'<[^>]*>', ' ', value or '')).split())


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


OPENER = urllib.request.build_opener(NoRedirect())


def request(url, headers=None):
    req = urllib.request.Request(url, headers={'User-Agent': AGENT, **(headers or {})})
    with OPENER.open(req, timeout=12) as response:
        body = response.read(4_000_001)
        if len(body) > 4_000_000:
            raise ValueError('response exceeds 4 MB')
        return body, response.headers


@lru_cache
def robots(origin):
    parser = urllib.robotparser.RobotFileParser()
    try:
        body, _ = request(origin + '/robots.txt')
        parser.parse(body.decode('utf-8', errors='replace').splitlines())
    except urllib.error.HTTPError as error:
        if error.code not in (404, 410):
            raise
        parser.parse([])
    return parser


def fetch(url, headers):
    parts = urlsplit(url)
    rules = robots(f'{parts.scheme}://{parts.netloc}')
    if not rules.can_fetch(AGENT, url):
        raise ValueError('blocked by robots.txt')
    delay = rules.crawl_delay(AGENT) or 0
    if delay > 20:
        raise ValueError('crawl delay exceeds collection window')
    for attempt in range(2):
        time.sleep(max(0.25, delay))
        try:
            return request(url, headers)
        except urllib.error.HTTPError as error:
            if error.code == 304:
                return None, error.headers
            if error.code not in (500, 502, 503, 504) or error.headers.get('Retry-After') or attempt:
                raise
        except OSError:
            if attempt:
                raise
        time.sleep(2)
    raise RuntimeError('unreachable')


def feed_rows(body):
    root = ET.fromstring(body)
    channel = root.find('channel')
    if channel is not None:
        for item in channel.findall('item'):
            yield item.findtext('title'), item.findtext('link'), item.findtext('pubDate'), item.findtext('description')
        return
    atom = '{http://www.w3.org/2005/Atom}'
    if root.tag != atom + 'feed':
        raise ValueError('unsupported feed XML')
    for entry in root.findall(atom + 'entry'):
        link = next((node.get('href') for node in entry.findall(atom + 'link')
                     if node.get('rel', 'alternate') == 'alternate'), None)
        yield (entry.findtext(atom + 'title'), link,
               entry.findtext(atom + 'published') or entry.findtext(atom + 'updated'),
               entry.findtext(atom + 'summary') or entry.findtext(atom + 'content'))


def timestamp(value):
    try:
        date = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError:
        date = parsedate_to_datetime(value)
    if date.tzinfo is None:
        raise ValueError('missing timezone')
    return date.astimezone(timezone.utc)


def collect(days=7, extra=(), only_extra=False, refresh=False):
    config = json.loads(subprocess.check_output([
        'node', '--input-type=module', '-e',
        "import {parse} from 'yaml'; import {readFileSync} from 'node:fs';"
        "console.log(JSON.stringify(parse(readFileSync('config/sources.yaml','utf8'))));",
    ]))['sources']
    config = list(extra) if only_extra else config + list(extra)
    items_path = Path('state/items.json')
    health_path = Path('.venture-runtime/health.json')
    items, health = load(items_path, {}), load(health_path, {})
    now = datetime.now(timezone.utc)
    known = {item['fingerprint']: key for key, item in items.items()}
    healthy = 0
    attempted = failed = duplicate = discovered = 0
    for source in config:
        key, kind = source['id'], source['kind']
        if source['category'] not in CATEGORIES or kind not in ('github', 'feed', 'discovery'):
            raise ValueError(f'{key}: invalid source configuration')
        if source.get('enabled') is False:
            continue
        url = ('https://api.github.com/repos/' + source['repo'] + '/releases?per_page=10'
               if kind == 'github' else source['url'])
        canonical(url)
        status = health.setdefault(key, {})
        if status.get('retry_after') and timestamp(status['retry_after']) > now:
            print(f'{key}: backoff', flush=True)
            continue
        validators = status.get('validators', {}) if status.get('url') == url and not refresh else {}
        attempted += 1
        try:
            body, headers = fetch(url, validators)
            if body is not None:
                rows = ((row['name'] or row['tag_name'], row['html_url'], row['published_at'], row['body'])
                        for row in json.loads(body) if not row['draft'] and not row['prerelease']) if kind == 'github' else feed_rows(body) if kind == 'feed' else ()
                if kind == 'discovery':
                    rows = source['parse'](body)
                for title, link, published, summary in rows:
                    if not (title and link and published):
                        continue
                    try:
                        date, link = timestamp(published), canonical(link)
                    except (ValueError, TypeError):
                        continue
                    if not now - timedelta(days=days) <= date <= now + timedelta(minutes=5):
                        continue
                    title, summary = clean(title)[:300], clean(summary)[:3200]
                    if not title or not summary:
                        continue
                    fingerprint = digest((title + '\n' + summary).casefold())
                    item_id = digest(link)
                    if item_id in items:
                        duplicate += 1
                        entry = items[item_id]
                        if entry['fingerprint'] != fingerprint:
                            entry.update(title=title, summary=summary[:3200], fingerprint=fingerprint,
                                         updated=now.isoformat())
                            known[fingerprint] = item_id
                        continue
                    if fingerprint in known:
                        duplicate += 1
                        continue
                    items[item_id] = dict(url=link, published=date.isoformat(), discovered=now.isoformat(),
                                          source=key, source_url=url, category=source['category'], title=title,
                                          summary=summary[:3200], fingerprint=fingerprint, status='pending')
                    known[fingerprint] = item_id
                    discovered += 1
                validators = {request_header: headers[response_header] for request_header, response_header in
                              [('If-None-Match', 'ETag'), ('If-Modified-Since', 'Last-Modified')] if response_header in headers}
            status.pop('first_failure', None)
            status.update(url=url, validators=validators, last_success=now.isoformat(), failures=0,
                          error=None, retry_after=None)
            healthy += 1
            print(f'{key}: {"unchanged" if body is None else "ok"}', flush=True)
        except (ValueError, OSError, ET.ParseError, KeyError, TypeError) as error:
            status.setdefault('first_failure', now.isoformat())
            failures = status.get('failures', 0) + 1
            delay = timedelta(hours=min(24, 2 ** min(failures - 1, 5)))
            if isinstance(error, urllib.error.HTTPError) and error.headers.get('Retry-After'):
                retry = error.headers['Retry-After']
                if retry.isdigit():
                    delay = max(delay, timedelta(seconds=int(retry)))
                else:
                    try:
                        delay = max(delay, timestamp(retry) - now)
                    except (TypeError, ValueError):
                        pass
            status.update(error=str(error), failures=failures, retry_after=(now + delay).isoformat())
            failed += 1
            print(f'{key}: {type(error).__name__}', flush=True)
    save(items_path, items)
    save(health_path, health)
    if 'RUNNER_TEMP' in os.environ:
        path = Path(os.environ['RUNNER_TEMP']) / 'venture' / 'collection.json'
        counts = load(path, {})
        for key, count in dict(attempted=attempted, succeeded=healthy, failed=failed,
                               duplicates=duplicate, discovered=discovered).items():
            counts[key] = counts.get(key, 0) + count
        save(path, counts)
    if not healthy:
        raise RuntimeError('no sources completed successfully')
    return items
