import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analytics import content, period, report, route, sync
from analytics_sources import RUM_PAGES, bing, cloudflare, cloudflare_settings, google, myna_billing
from analytics_review import valid
from collect import save
from editor import metadata
from model_cost import estimate, event_usage

PRICE = dict(input_per_million=2, cached_input_per_million=1, output_per_million=4,
             currency='USD', cache_in_input=True, reasoning_in_output=True)
USAGE = dict(input_tokens=100, cached_input_tokens=20, output_tokens=50, reasoning_output_tokens=25)


class AnalyticsTests(unittest.TestCase):
    def test_actual_content(self):
        rows = metadata()
        data = content(rows)
        self.assertEqual(data['total'], len(list(Path('src/content').glob('*/*.md'))))
        self.assertEqual(sum(data['days'].values()), data['total'])
        self.assertEqual(data['source_coverage'], 1)
        self.assertEqual(route('https://codex-venture.com/news/example?a=1#fragment'), '/news/example/')
        self.assertIsNone(route('https://elsewhere.test/news/example/'))

    def test_myna_billing_paginates_and_rejects_duplicate_records(self):
        day = date(2026, 11, 24)
        start = int(datetime(2026, 11, 24, tzinfo=timezone.utc).timestamp())
        first = {'id': 1, 'created_at': start, 'model': 'codex', 'cost': '0.10'}
        second = {**first, 'id': 2, 'cost': '0.20'}
        pages = [{'count': 2, 'token_usages': [row]} for row in (first, second)]
        with patch.dict(os.environ, {'CODEX_API_KEY': 'fixture'}):
            with patch('analytics_sources.api', side_effect=pages) as request:
                self.assertEqual(myna_billing(day, timezone.utc)['data']['amount'], '0.30')
                self.assertIn('offset=1', request.call_args.args[0])
            with patch('analytics_sources.api', side_effect=[pages[0], pages[0]]):
                self.assertEqual(myna_billing(day, timezone.utc)['status'], 'unavailable')

    def test_cost(self):
        usage = event_usage([{'type': 'turn.completed', 'usage': USAGE}])
        self.assertEqual(usage, USAGE)
        self.assertEqual(estimate(usage, PRICE), {'currency': 'USD', 'amount': '0.00038'})
        self.assertEqual(estimate(usage, {**PRICE, 'cache_in_input': False,
                                         'reasoning_in_output': False})['amount'], '0.00052')
        self.assertIsNone(estimate(usage, None))
        self.assertIsNone(event_usage([{'type': 'turn.failed'}]))
        self.assertIsNone(estimate({'input_tokens': 1, 'output_tokens': 2}, PRICE))

    def test_unconfigured_and_idempotent_reports(self):
        with TemporaryDirectory() as location, patch.dict(os.environ, {}, clear=True):
            self.assertEqual([cloudflare('2026-11-23'), google('2026-11-23'), bing()],
                             [{'status': 'disabled'}] * 3)
            root = Path(location)
            today = date(2026, 11, 24)
            sync(root, 'traffic', today, 2)
            initial = {p.name: p.read_bytes() for p in (root / 'traffic').glob('*.json')}
            sync(root, 'traffic', today, 2)
            self.assertEqual(initial, {p.name: p.read_bytes() for p in (root / 'traffic').glob('*.json')})
            for task in ('daily', 'weekly', 'monthly'):
                start, end = period(task, today)
                result = report(root, start, end, content([]))
                save(root / f'{task}.json', result)
                self.assertEqual(result['observed_days'], {})
                self.assertEqual(sum(result['new_articles'].values()), 0)
            self.assertEqual(period('monthly', date(2026, 1, 1)),
                             (date(2025, 12, 1), date(2025, 12, 31)))

    def test_strategy_constraints(self):
        baseline = {'category_weights': {'models': 1}, 'candidate_limit': 8, 'max_articles': 2}
        self.assertTrue(valid(baseline))
        self.assertFalse(valid({**baseline, 'budget': 999}))
        self.assertFalse(valid({**baseline, 'category_weights': {'models': -20}}))

    def test_cloudflare_settings_gate_and_retention(self):
        def account_response(token, account, query, **variables):
            if 'settings' in query:
                dataset = RUM_PAGES if RUM_PAGES in query else 'rumWebVitalsEventsAdaptiveGroups'
                return {'settings': {dataset: dict(enabled=dataset == RUM_PAGES,
                         availableFields=['count'], maxPageSize=10,
                         notOlderThan=3 * 86400, maxDuration=86400)}}
            self.assertIn('{ count }', query)
            return {'rows': [{'count': 7}]}

        env = {'CLOUDFLARE_ANALYTICS_TOKEN': 'fixture', 'CLOUDFLARE_ACCOUNT_ID': 'fixture',
               'CLOUDFLARE_WEB_ANALYTICS_SITE_TAG': 'fixture'}
        cloudflare_settings.cache_clear()
        self.addCleanup(cloudflare_settings.cache_clear)
        with patch.dict(os.environ, env, clear=True), patch(
                'analytics_sources.cloudflare_account', side_effect=account_response) as api:
            today = datetime.now(timezone.utc).date()
            recent = cloudflare((today - timedelta(days=1)).isoformat())
            self.assertEqual(recent['metrics']['page_views']['data'][0]['count'], 7)
            self.assertEqual(recent['metrics']['visits']['status'], 'unavailable')
            self.assertEqual(cloudflare((today - timedelta(days=5)).isoformat())['status'], 'unavailable')
            self.assertEqual(api.call_count, 3)


if __name__ == '__main__':
    unittest.main()
