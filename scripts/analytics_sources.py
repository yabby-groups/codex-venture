"""Read-only provider adapters. Store each provider's native date and metric definitions."""
import json
import os
from datetime import date, datetime, timedelta, timezone
from functools import lru_cache
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


def api(url, token=None, data=None, method=None):
    headers = {'Accept': 'application/json', 'User-Agent': 'Codex-Venture-Analytics'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    if data is not None:
        headers['Content-Type'] = 'application/json'
        data = json.dumps(data).encode()
    with urlopen(Request(url, data, headers, method=method), timeout=25) as response:
        return json.load(response)


def result(read):
    try:
        return {'status': 'available', 'data': read()}
    except (OSError, ValueError, KeyError, TypeError, RuntimeError) as error:
        return {'status': 'unavailable', 'reason': type(error).__name__,
                'http_status': getattr(error, 'code', None)}


RUM_PAGES = 'rumPageloadEventsAdaptiveGroups'
RUM_VITALS = 'rumWebVitalsEventsAdaptiveGroups'


def cloudflare_account(token, account, query, **variables):
    response = api('https://api.cloudflare.com/client/v4/graphql', token,
                   {'query': query, 'variables': {'account': account, **variables}})
    if response.get('errors'):
        raise RuntimeError('GraphQL dataset or field unavailable')
    accounts = response['data']['viewer']['accounts']
    if not accounts:
        raise RuntimeError('Cloudflare account unavailable')
    return accounts[0]


@lru_cache(maxsize=4)
def cloudflare_settings(token, account, dataset):
    query = '''
    query($account: string) {
      viewer { accounts(filter: {accountTag: $account}) {
        settings { DATASET { enabled availableFields maxPageSize notOlderThan maxDuration } }
      } }
    }'''.replace('DATASET', dataset)
    return result(lambda: cloudflare_account(token, account, query)['settings'][dataset])


def cloudflare(day):
    token = os.getenv('CLOUDFLARE_ANALYTICS_TOKEN')
    account = os.getenv('CLOUDFLARE_ACCOUNT_ID')
    tag = os.getenv('CLOUDFLARE_WEB_ANALYTICS_SITE_TAG')
    if not all((token, account, tag)):
        return {'status': 'disabled'}

    capabilities = {dataset: cloudflare_settings(token, account, dataset)
                    for dataset in (RUM_PAGES, RUM_VITALS)}
    start = datetime.fromisoformat(day).replace(tzinfo=timezone.utc)

    def query(dataset, fields, required, limit=1, extra=''):
        capability = capabilities[dataset].get('data') or {}
        if capability:
            if not capability['enabled'] or not set(required) <= set(capability['availableFields']):
                raise RuntimeError('Metric disabled by account settings')
            if (capability['maxDuration'] < 86400 or
                    start < datetime.now(timezone.utc) - timedelta(seconds=capability['notOlderThan'])):
                raise RuntimeError('Date outside dataset limits')
            limit = min(limit, capability['maxPageSize'])
        query_text = '''
        query($account: string, $site: string, $start: Time, $end: Time) {
          viewer { accounts(filter: {accountTag: $account}) {
            rows: DATASET(limit: LIMIT, filter: {
              siteTag: $site, datetime_geq: $start, datetime_lt: $end
            } EXTRA) { FIELDS }
          } }
        }'''.replace('DATASET', dataset).replace('LIMIT', str(limit)).replace(
            'FIELDS', fields).replace('EXTRA', extra)
        end = (date.fromisoformat(day) + timedelta(days=1)).isoformat()
        return cloudflare_account(token, account, query_text, site=tag,
                                  start=day + 'T00:00:00Z', end=end + 'T00:00:00Z')['rows']

    metrics = {
        'page_views': result(lambda: query(RUM_PAGES, 'count', ['count'])),
        'visits': result(lambda: query(RUM_PAGES, 'sum { visits }', ['sum_visits'])),
    }
    for key, dimension in {'pages': 'requestPath', 'referrers': 'refererHost',
                           'countries': 'countryName', 'devices': 'deviceType',
                           'browsers': 'userAgentBrowser'}.items():
        metrics[key] = result(lambda: query(RUM_PAGES, f'dimensions {{ {dimension} }} count',
                                            ['dimensions_' + dimension, 'count'],
                                            100, ', orderBy: [count_DESC]'))
    for field in ('largestContentfulPaintP75', 'interactionToNextPaintP75',
                  'cumulativeLayoutShiftP75', 'firstContentfulPaintP75', 'timeToFirstByteP75'):
        metrics[field] = result(lambda: query(RUM_VITALS, f'quantiles {{ {field} }}',
                                              ['quantiles_' + field]))
    metrics['unique_visitors'] = {'status': 'unavailable'}
    return {'status': 'available' if any(v['status'] == 'available' for v in metrics.values())
            else 'unavailable', 'timezone': 'UTC', 'source': 'Cloudflare RUM', 'metrics': metrics,
            'capabilities': capabilities}


def google(day, inspection_urls=()):
    token = os.getenv('GOOGLE_ACCESS_TOKEN')
    property_id = os.getenv('GOOGLE_SEARCH_CONSOLE_PROPERTY')
    if not token or not property_id:
        return {'status': 'disabled'}
    root = 'https://searchconsole.googleapis.com'
    endpoint = root + '/webmasters/v3/sites/' + quote(property_id, safe='') + '/searchAnalytics/query'

    def query(dimension):
        response = api(endpoint, token, dict(startDate=day, endDate=day, type='web',
                                            dataState='final', rowLimit=1000,
                                            dimensions=[dimension] if dimension else []))
        return {'rows': response.get('rows', []), 'possibly_truncated': len(response.get('rows', [])) == 1000}

    metrics = {key or 'totals': result(lambda: query(key))
               for key in ('', 'query', 'page', 'country', 'device')}
    inspections = {}
    for url in inspection_urls:
        inspections[url] = result(lambda: api(root + '/v1/urlInspection/index:inspect', token,
                                             {'inspectionUrl': url, 'siteUrl': property_id})
                                  ['inspectionResult']['indexStatusResult'])
    return {'status': metrics['totals']['status'], 'timezone': 'America/Los_Angeles',
            'metrics': metrics, 'inspection_at_sync': inspections}


def bing():
    token, site = os.getenv('BING_WEBMASTER_API_KEY'), os.getenv('BING_SITE_URL')
    if not token or not site:
        return {'status': 'disabled'}

    def query(operation):
        params = urlencode({'siteUrl': site, 'apikey': token})
        return api('https://ssl.bing.com/webmaster/api.svc/json/' + operation + '?' + params)['d']

    metrics = {key: result(lambda: query(operation)) for key, operation in {
        'totals': 'GetRankAndTrafficStats', 'pages': 'GetPageStats',
        'queries': 'GetQueryStats', 'crawl_index': 'GetCrawlStats',
    }.items()}
    return {'status': metrics['totals']['status'], 'metrics': metrics,
            'timezone': 'provider', 'dates': 'provider-native rolling snapshot'}
