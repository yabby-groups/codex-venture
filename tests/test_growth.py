from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import analytics_review
from collect import load, save
from growth import distribution, HN_TOPIC, question_rows, similar, tokens


class GrowthTests(unittest.TestCase):
    def test_old_strategy_preserves_review_gate(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            save(root / 'strategy/current.json', {
                'category_weights': {'coding': 1}, 'candidate_limit': 12,
                'max_articles': 1, 'reader_review': {'publish': 1},
            })
            with patch.object(analytics_review, 'store', return_value=root):
                strategy = analytics_review.strategy()
            self.assertEqual(strategy['version'], 1)
            self.assertEqual(strategy['candidate_limit'], 12)
            self.assertEqual(strategy['reader_review']['publish'], 75)
            self.assertNotIn('max_articles', strategy)

    def test_question_relevance_and_duplicate(self):
        rows = [('Ask HN: How can I run local LLMs?', '', '', '', {}),
                ('Ask HN: How do recruiters work?', '', '', '', {})]
        self.assertEqual(len(list(question_rows(lambda _: rows, HN_TOPIC)(None))), 1)
        self.assertTrue(similar(tokens(rows[0][0]), tokens('Run local LLMs')))

    def test_distribution_is_idempotent_for_same_content(self):
        article = {'slug': 'local-ai', 'collection': 'news', 'titleEn': 'Local AI',
                   'summaryEn': 'A local AI test with useful detail.'}
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(distribution(root, ['news/local-ai/'], [article], 'first'), 1)
            self.assertEqual(distribution(root, ['/news/local-ai/'], [article], 'second'), 0)
            draft = load(next(root.glob('distribution/*.json')), {})
            self.assertEqual(draft['sha'], 'first')
            self.assertIn('utm_source=bluesky', draft['variants']['bluesky']['text'])
