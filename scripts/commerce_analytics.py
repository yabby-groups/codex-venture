"""Private daily provider snapshots with independent native date and metric scopes."""
from collections import Counter
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
import json
import os
import re
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from analytics_sources import api, result


def google_token(prefix):
    token = os.getenv(prefix + '_ACCESS_TOKEN')
    if token:
        return token
    fields = {key: os.getenv(prefix + '_' + key.upper())
              for key in ('client_id', 'client_secret', 'refresh_token')}
    if not all(fields.values()):
        return None
    request = Request('https://oauth2.googleapis.com/token',
                      urlencode({**fields, 'grant_type': 'refresh_token'}).encode(),
                      {'Content-Type': 'application/x-www-form-urlencoded'})
    with urlopen(request, timeout=25) as response:
        return json.load(response)['access_token']


def ga4(day):
    property_id = os.getenv('GOOGLE_GA4_PROPERTY_ID', '')
    if not re.fullmatch(r'[0-9]+', property_id):
        return {'status': 'disabled'}
    token = os.getenv('GOOGLE_GA4_ACCESS_TOKEN') or result(lambda: google_token('GOOGLE_GA4')).get('data')
    if not token:
        return {'status': 'unavailable'}

    def query(dimensions, metrics):
        endpoint = f'https://analyticsdata.googleapis.com/v1beta/properties/{property_id}:runReport'
        response = api(endpoint, token, {
            'dateRanges': [{'startDate': day, 'endDate': day}],
            'dimensions': [{'name': name} for name in dimensions],
            'metrics': [{'name': name} for name in metrics],
            'orderBys': [{'metric': {'metricName': metrics[0]}, 'desc': True}],
            'limit': 100,
        })
        return {key: response[key] for key in
                ('rows', 'rowCount', 'metadata', 'dimensionHeaders', 'metricHeaders') if key in response}

    metrics = {
        'totals': result(lambda: query([], ['sessions', 'activeUsers', 'screenPageViews', 'keyEvents'])),
        'sources': result(lambda: query(['sessionSourceMedium'], ['sessions', 'keyEvents'])),
        'pages': result(lambda: query(['pagePath'], ['screenPageViews', 'userEngagementDuration', 'activeUsers'])),
        'content_events': result(lambda: query(['eventName', 'pagePath'], ['eventCount'])),
        'audience': result(lambda: query(['newVsReturning'], ['activeUsers', 'userEngagementDuration'])),
        'recommendations': result(lambda: query(['eventName', 'customEvent:destination'], ['eventCount'])),
    }
    return {'status': metrics['totals']['status'], 'timezone': 'GA4 property setting',
            'scope': 'Consented GA4 activity', 'metrics': metrics}


def adsense(day):
    account = os.getenv('GOOGLE_ADSENSE_ACCOUNT', '')
    if not re.fullmatch(r'accounts/pub-[0-9]{16}', account):
        return {'status': 'disabled'}

    def read():
        token = google_token('GOOGLE_ADSENSE')
        if not token:
            raise ValueError('AdSense OAuth unavailable')
        parts = date.fromisoformat(day)
        params = [(name + '.' + key, getattr(parts, key)) for name in ('startDate', 'endDate')
                  for key in ('year', 'month', 'day')]
        params += [('metrics', key) for key in ('ESTIMATED_EARNINGS', 'IMPRESSIONS', 'CLICKS')]
        params += [('dimensions', 'DATE'), ('reportingTimeZone', 'ACCOUNT_TIME_ZONE'),
                   ('filters', 'DOMAIN_NAME==codex-venture.com')]
        response = api(f'https://adsense.googleapis.com/v2/{account}/reports:generate?' + urlencode(params), token)
        return {key: response[key] for key in ('headers', 'rows', 'totals', 'warnings') if key in response}

    return {**result(read), 'timezone': 'AdSense account setting', 'scope': 'Estimated site earnings'}


def edge(day):
    zone = os.getenv('CLOUDFLARE_ZONE_ID')
    token = os.getenv('CLOUDFLARE_ZONE_ANALYTICS_TOKEN') or os.getenv('CLOUDFLARE_ANALYTICS_TOKEN')
    if not zone or not token:
        return {'status': 'disabled'}

    def query(fields, limit, condition=''):
        gql = '''
        query($zone: string, $start: Time, $end: Time) {
          viewer { zones(filter: {zoneTag: $zone}) {
            rows: httpRequestsAdaptiveGroups(limit: LIMIT, filter: {
              datetime_geq: $start, datetime_lt: $end, clientRequestHTTPHost: "codex-venture.com"
              CONDITION
            }, orderBy: [count_DESC]) { count dimensions { FIELDS } }
          } }
        }'''.replace('LIMIT', str(limit)).replace('FIELDS', fields).replace('CONDITION', condition)
        response = api('https://api.cloudflare.com/client/v4/graphql', token, {
            'query': gql, 'variables': {'zone': zone, 'start': day + 'T00:00:00Z',
                                        'end': str(date.fromisoformat(day) + timedelta(days=1)) + 'T00:00:00Z'}})
        if response.get('errors'):
            raise RuntimeError('Cloudflare zone dataset or field unavailable')
        rows = response['data']['viewer']['zones'][0]['rows']
        return {'rows': rows, 'possibly_truncated': len(rows) == limit}

    metrics = {
        'status': result(lambda: query('edgeResponseStatus', 100)),
        '4xx_paths': result(lambda: query('edgeResponseStatus clientRequestPath', 50,
                                         'edgeResponseStatus_geq: 400, edgeResponseStatus_lt: 500')),
        'hourly': result(lambda: query('datetimeHour', 24)),
        'ports': result(lambda: query('clientRequestPort', 100)),
    }
    return {'status': ('available' if any(value['status'] == 'available' for value in metrics.values())
                       else 'unavailable'), 'timezone': 'UTC',
            'scope': 'Cloudflare edge request groups (may be sampled)', 'metrics': metrics}


SEARCH = re.compile(r'googlebot|bingbot|duckduckbot|yandexbot|baiduspider|applebot(?!-extended)', re.I)
AI = re.compile(r'gptbot|oai-searchbot|chatgpt-user|claudebot|claude-searchbot|claude-user|'
                r'perplexitybot|perplexity-user|google-extended|applebot-extended|ccbot|'
                r'amazonbot|bytespider|meta-externalagent', re.I)
TEST = re.compile(r'CodexVentureMonitor|Codex-Venture-Test|HeadlessChrome|Playwright', re.I)


def classify(row):
    ua = row.get('user_agent', '')
    if TEST.search(ua):
        return 'automation_test'
    if AI.search(ua):
        return 'verified_ai_crawler' if row.get('verified_bot') is True else 'claimed_ai_crawler'
    if SEARCH.search(ua):
        return 'verified_search_crawler' if row.get('verified_bot') is True else 'claimed_search_crawler'
    if row.get('verified_bot') is True:
        return 'other_verified_bot'
    if row.get('port') not in (None, 80, 443) or row.get('status') in (403, 429) or not ua:
        return 'anomalous_request'
    if 'Mozilla/' in ua:
        return 'browser_like_unverified'
    return 'unclassified'


def exported_requests(path):
    """Read normalized operator-provided observations, keeping only aggregate counts."""
    if not path.is_file():
        return {'status': 'disabled'}
    def read():
        classes, errors, hours, ports = Counter(), Counter(), Counter(), Counter()
        with path.open() as handle:
            for line in handle:
                row = json.loads(line)
                classes[classify(row)] += 1
                if isinstance(row.get('status'), int) and 400 <= row['status'] < 500:
                    errors[row['status']] += 1
                if row.get('port') is not None:
                    ports[int(row['port'])] += 1
                if isinstance(row.get('timestamp'), str):
                    hours[row['timestamp'][:13]] += 1
        return {'classes': classes, '4xx_status': errors, 'ports': ports, 'hours': hours}
    return {**result(read), 'scope': 'Exported observations, coverage provider-dependent'}


def affiliate(path):
    if not path.is_file():
        return {'status': 'disabled'}
    def read():
        records = json.loads(path.read_text())
        if not isinstance(records, list):
            raise ValueError('Expected affiliate report rows')
        rows = []
        for row in records:
            count = row['conversions']
            currency = row['currency']
            try:
                amount = Decimal(str(row['commission']))
            except InvalidOperation as error:
                raise ValueError('Invalid affiliate commission') from error
            if type(count) is not int or count < 0 or not re.fullmatch('[A-Z]{3}', currency) or not amount.is_finite():
                raise ValueError('Invalid affiliate totals')
            rows.append(dict(program=str(row['program']), conversions=count,
                             currency=currency, commission=str(amount)))
        return rows
    return {**result(read), 'scope': 'Network-reported conversions and commission'}
