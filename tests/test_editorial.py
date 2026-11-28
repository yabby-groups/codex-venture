import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import editorial
import hosted
import original


class EditorialTests(unittest.TestCase):
    def test_community_demand_is_eligible_before_primary_evidence(self):
        item = dict(status='pending', content_type='tutorials', discovery={'demand_id': 'demand'})
        self.assertIs(original.ready('practices', item), True)
        self.assertIs(original.ready('stories', item), False)
        item['discovery'] = {}
        self.assertIs(original.ready('practices', item), False)

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

    def test_traced_selection_requires_candidate_reason(self):
        self.batch['selectionVersion'] = 3
        with patch.object(hosted, 'model_call', return_value={'pitches': [], 'rejections': []}):
            with self.assertRaisesRegex(ValueError, 'exactly one disposition'):
                hosted.run_model(self.batch, False, {})
        result = {'pitches': [], 'rejections': [{'id': 'candidate', 'reason': 'Already covered'}]}
        receipt = {}
        with patch.object(hosted, 'model_call', return_value=result) as model:
            hosted.run_model(self.batch, False, receipt)
        self.assertEqual(model.call_count, 1)
        self.assertEqual(receipt['candidate_dispositions']['rejections'][0]['reason'], 'Already covered')

    def test_traced_writer_must_explain_empty_draft(self):
        self.batch['selectionVersion'] = 3
        pitch = dict.fromkeys(editorial.PITCH['properties']['pitches']['items']['required'], 'reason')
        pitch.update(id='candidate', audience='core', researchGap='', researchUrl='')
        selection = {'pitches': [pitch], 'rejections': []}
        draft = {'articles': [], 'unwritten': [{'id': 'candidate', 'reason': 'Evidence was removed'}]}
        receipt = {}
        with patch.object(hosted, 'model_call', side_effect=[selection, draft]) as model:
            hosted.run_model(self.batch, False, receipt)
        self.assertEqual(model.call_count, 2)
        self.assertEqual(receipt['candidate_dispositions']['unwritten'][0]['reason'], 'Evidence was removed')

    def test_scores_and_hard_gates(self):
        self.assertEqual(editorial.decisions(self.draft, self.review, {})[1],
                         {'article': dict(score=100, tier='lead', audience='core')})
        row = self.review['reviews'][0]
        row['gates']['evidence'] = False
        self.assertEqual(editorial.decisions(self.draft, self.review, {}), ([], {}))
        row['gates']['evidence'] = True
        row['scores']['utility'] = 0
        row['scores']['interest'] = 24
        self.assertEqual(editorial.decisions(self.draft, self.review, {})[0], [self.article])
        row['actionable'] = False
        self.assertEqual(editorial.decisions(self.draft, self.review, {}), ([], {}))
        with self.assertRaisesRegex(ValueError, 'cover each draft'):
            editorial.decisions(self.draft, {'reviews': []}, {})

    def test_sharpe_article_cannot_be_recommended_as_vertical(self):
        path = Path(__file__).resolve().parents[1] / 'src/content/news/audit-sharpe-annualization-before-strategy-promotion.md'
        self.article.update(slug=path.stem, body=path.read_text())
        self.review['reviews'][0].update(slug=path.stem, audience='vertical')
        published, ratings = editorial.decisions(self.draft, self.review, {})
        self.assertEqual(published, [self.article])
        self.assertEqual(ratings[path.stem]['tier'], 'standard')
