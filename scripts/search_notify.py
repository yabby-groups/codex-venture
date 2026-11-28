"""Submit verified, changed public article routes to IndexNow."""
import json
from pathlib import Path
import re
import urllib.request

from collect import digest, save
from geo import request, SITE


def indexnow(root, routes):
    key = Path(__file__).resolve().parent.parent / 'config/indexnow-key.txt'
    if not key.is_file():
        return {'status': 'blocked', 'reason': 'IndexNow key hosting is not configured'}
    value = key.read_text().strip()
    if not re.fullmatch(r'[a-f0-9]{32}', value):
        raise ValueError('Invalid IndexNow key')
    paths = sorted({'/' + route.strip('/') + '/' for route in routes
                    if re.fullmatch(r'/?(?:news|daily)/[a-z0-9-]+/?', route)})
    if not paths:
        return {'status': 'skipped'}
    if request('/' + value + '.txt').strip() != value:
        raise ValueError('Production IndexNow key does not match')
    urls = [SITE + path for path in paths]
    versions = [digest(request(path)) for path in paths]
    receipt = root / (digest(json.dumps([urls, versions])) + '.json')
    if receipt.exists():
        return {'status': 'already_submitted'}
    payload = {'host': 'codex-venture.com', 'key': value,
               'keyLocation': SITE + '/' + value + '.txt', 'urlList': urls}
    submission = urllib.request.Request('https://api.indexnow.org/indexnow',
        data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json; charset=utf-8'})
    with urllib.request.urlopen(submission, timeout=20) as response:
        if response.status not in (200, 202):
            raise ValueError(f'Unexpected IndexNow status {response.status}')
        result = {'status': 'submitted', 'http_status': response.status, 'urls': urls}
    save(receipt, result)
    return result
