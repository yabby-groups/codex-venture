"""Read-only provider adapters. Store each provider's native date and metric definitions."""
import json
import os
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


def cloudflare(day):
    token = os.getenv('CLOUDFLARE_ANALYTICS_TOKEN')
    account = os.getenv('CLOUDFLARE_ACCOUNT_ID')
    tag = os.getenv('CLOUDFLARE_WEB_ANALYTICS_SITE_TAG')
    if not all((token, account, tag)):
        return {'status': 'disabled'}

    def query(dataset, fields, limit=1, extra=''):
        query_text = '''
        query($account: string, $site: string, $start: Time, $end: Time) {
          viewer { accounts(filter: {accountTag: $account}) {
            rows: DATASET(limit: LIMIT, filter: {
              siteTag: $site, datetime_geq: $start, datetime_lt: $end
            } EXTRA) { FIELDS }
          } }
        }'''.replace('DATASET', dataset).replace('LIMIT', str(limit)).replace(
            'FIELDS', fields).replace('EXTRA', extra)
        from datetime import timedelta, date
        end = (date.fromisoformat(day) + timedelta(days=1)).isoformat()
        response = api('https://api.cloudflare.com/client/v4/graphql', token,
                       {'query': query_text, 'variables': {
                           'account': account, 'site': tag, 'start': day + 'T00:00:00Z',
                           'end': end + 'T00:00:00Z'}})
        if response.get('errors'):
            raise RuntimeError('GraphQL dataset or field unavailable')
        return response['data']['viewer']['accounts'][0]['rows']

    dataset = 'rumPageloadEventsAdaptiveGroups'
    fields = {
        'page_views': 'sum { pageViews }', 'visits': 'sum { visits }',
        'load_performance_ms': 'quantiles { pageLoadTimeP50 pageLoadTimeP75 pageLoadTimeP95 }',
    }
    metrics = {key: result(lambda: query(dataset, select)) for key, select in fields.items()}
    for key, dimension in {'pages': 'requestPath', 'referrers': 'refererHost',
                           'countries': 'countryName', 'devices': 'deviceType',
                           'browsers': 'browserName'}.items():
        metrics[key] = result(lambda: query(dataset, f'dimensions {{ {dimension} }} sum {{ pageViews }}',
                                            100, ', orderBy: [sum_pageViews_DESC]'))
    metrics['core_web_vitals'] = result(lambda: query(
        'rumWebVitalsEventsAdaptiveGroups', 'quantiles { lcpP75 inpP75 clsP75 }'))
    metrics['unique_visitors'] = {'status': 'unavailable'}
    return {'status': 'available' if any(v['status'] == 'available' for v in metrics.values())
            else 'unavailable', 'timezone': 'UTC', 'source': 'Cloudflare RUM', 'metrics': metrics}


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
