import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from analytics import commercial_day, period
from commerce_analytics import adsense, classify, edge
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

    def test_daily_uses_closed_day(self):
        self.assertEqual(period('daily', date(2026, 11, 27)), (date(2026, 11, 26),) * 2)
