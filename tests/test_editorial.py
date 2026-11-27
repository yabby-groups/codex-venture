import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import editorial
import hosted


class EditorialTests(unittest.TestCase):
    def setUp(self):
        self.article = dict.fromkeys(
            ('slug', 'titleZh', 'titleEn', 'summaryZh', 'summaryEn', 'category', 'body', 'type', 'version'),
            'article',
        )
        self.article.update(tags=[], itemIds=['candidate'], blocks=[], resourceIds=[])
        self.draft = dict(articles=[self.article], skipped=[])
        self.review = {'reviews': [dict(slug='article', grounds='Explains a concrete workflow.',
                                       actionable=True, audience='core', scores=dict(editorial.DIMENSIONS),
                                       gates=dict.fromkeys(editorial.GATES, True))]}
        self.batch = dict(task='news', candidates={'candidate': {}}, existingResources=[], unlimited=True, enforce_cost_limit=False)

    def test_empty_selection_ends_model_run(self):
        with patch.object(hosted, 'model_call', return_value={'pitches': []}) as model:
            response = hosted.run_model(self.batch, False, {})
        self.assertEqual(response['draft']['articles'], [])
        self.assertEqual(model.call_count, 1)

    def test_selection_draft_review_run_independently(self):
        pitch = dict.fromkeys(editorial.PITCH['properties']['pitches']['items']['required'], 'reason')
        pitch.update(id='candidate', audience='core', researchGap='', researchUrl='')
        with patch.object(hosted, 'model_call', side_effect=[{'pitches': [pitch]}, self.draft, self.review]) as model:
            response = hosted.run_model(self.batch, False, {})
        self.assertEqual([call.kwargs['stage'] for call in model.call_args_list],
                         ['editorial-selection', 'editor', 'reader-review'])
        self.assertEqual(model.call_args.kwargs['payload_override']['articles'], self.draft['articles'])
        self.assertEqual(response['review'], self.review)

    def test_scores_and_hard_gates(self):
        self.assertEqual(editorial.decisions(self.draft, self.review, {})[1],
                         {'article': dict(score=100, tier='lead', audience='core')})
        row = self.review['reviews'][0]
        row['gates']['evidence'] = False
        self.assertEqual(editorial.decisions(self.draft, self.review, {}), ([], {}))
        row['gates']['evidence'] = True
        row['scores']['utility'] = 0
        row['scores']['interest'] = 24
        self.assertEqual(editorial.decisions(self.draft, self.review, {}), ([], {}))
        with self.assertRaisesRegex(ValueError, 'cover each draft'):
            editorial.decisions(self.draft, {'reviews': []}, {})
