import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from analytics import commercial_day, content, period, report, sync_commerce
from commerce_analytics import adsense, classify, edge, ga4
from datetime import date


class CommerceAnalyticsTests(unittest.TestCase):
    def test_unverified_browser_and_claimed_bots(self):
        self.assertEqual(classify({'user_agent': 'Mozilla/5.0'}), 'browser_like_unverified')
        self.assertEqual(classify({'user_agent': 'Mozilla GPTBot'}), 'claimed_ai_crawler')
        self.assertEqual(classify({'user_agent': 'Googlebot', 'verified_bot': True}), 'verified_search_crawler')
        self.assertEqual(classify({'user_agent': 'Codex-Venture-Test'}), 'automation_test')
        self.assertEqual(classify({'user_agent': 'Mozilla/5.0', 'port': 8443}), 'anomalous_request')

    def test_missing_and_invalid_observations_remain_unknown(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            day = '2026-11-26'
            path = root / 'imports/affiliate' / (day + '.json')
            path.parent.mkdir(parents=True)
            path.write_text('[{"program":"test","conversions":0,"currency":"USD","commission":"bad"}]')
            self.assertTrue(all(value == 'UNKNOWN' for value in commercial_day(root, day).values()))

    def test_edge_and_adsense_provider_payloads(self):
        with patch.dict(os.environ, {'CLOUDFLARE_ZONE_ID': 'zone', 'CLOUDFLARE_ZONE_ANALYTICS_TOKEN': 'token'}):
            response = {'data': {'viewer': {'zones': [{'rows': []}]}}}
            with patch('commerce_analytics.api', return_value=response) as api:
                snapshot = edge('2026-11-26')
                self.assertEqual(snapshot['metrics']['ports']['status'], 'available')
                self.assertIn('edgeResponseStatus_geq: 400', api.call_args_list[1].args[2]['query'])
        with patch.dict(os.environ, {'GOOGLE_ADSENSE_ACCOUNT': 'accounts/pub-1234567890123456'}):
            with patch('commerce_analytics.google_token', return_value='token'), patch(
                'commerce_analytics.api', return_value={'rows': []}
            ) as api:
                self.assertEqual(adsense('2026-11-26')['status'], 'available')
                self.assertIn('DOMAIN_NAME%3D%3Dcodex-venture.com', api.call_args.args[0])

    @patch.dict(os.environ, {'GOOGLE_GA4_PROPERTY_ID': '123456789'})
    @patch('commerce_analytics.google_token', return_value='fixture-token')
    @patch('commerce_analytics.api')
    def test_ga4_fixture_flows_into_all_report_periods(self, api, token):
        day = '2026-11-26'
        api.return_value = {'rowCount': 1, 'rows': [{'metricValues': [
            {'value': value} for value in ('2', '2', '3', '0')
        ]}]}
        snapshot = ga4(day)
        token.assert_called_once_with('GOOGLE_GA4')
        self.assertEqual(api.call_count, 3)
        endpoint, access_token, payload = api.call_args_list[0].args
        self.assertTrue(endpoint.endswith('/123456789:runReport'))
        self.assertEqual(access_token, 'fixture-token')
        self.assertEqual(payload['dateRanges'], [{'startDate': day, 'endDate': day}])
        self.assertEqual(snapshot['status'], 'available')
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with patch('analytics.ga4', side_effect=[snapshot, {'status': 'unavailable'}]), patch(
                'analytics.adsense', return_value={'status': 'disabled'}
            ), patch('analytics.edge', return_value={'status': 'disabled'}):
                sync_commerce(root, [day])
                sync_commerce(root, [day])
            for task, today in [('daily', date(2026, 11, 27)), ('weekly', date(2026, 11, 30)),
                                ('monthly', date(2026, 12, 1))]:
                with self.subTest(task=task):
                    start, end = period(task, today)
                    data = report(root, start, end, content([]))
                    self.assertEqual(data['monetization'][day]['ga4'], snapshot)

    @patch.dict(os.environ, {'GOOGLE_GA4_PROPERTY_ID': '123456789'})
    @patch('commerce_analytics.google_token', return_value=None)
    @patch('commerce_analytics.api')
    def test_ga4_without_oauth_makes_no_report_request(self, api, token):
        self.assertEqual(ga4('2026-11-26'), {'status': 'unavailable'})
        api.assert_not_called()

    def test_daily_uses_closed_day(self):
        self.assertEqual(period('daily', date(2026, 11, 27)), (date(2026, 11, 26),) * 2)
