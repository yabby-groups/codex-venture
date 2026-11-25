import json
import sys
import tempfile
import time
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, 'scripts')

import editor
import evidence
import resource_ingest as ingest


class ResourceOperations(unittest.TestCase):
    def test_multiline_yaml_and_resumable_skill_scan(self):
        yaml = '---\nname: "文档"\ndescription: |\n  First line\n  第二行\n---\nbody'
        self.assertEqual(evidence.skill_metadata(yaml)['description'], 'First line\n第二行')
        paths = {f'skills/{i}/SKILL.md': f'sha{i}' for i in range(11)}
        item = dict(discovery={}, source='test', category='agents', published='2026-11-25')

        def document(url, **_):
            if '/git/blobs/' in url:
                if url.endswith('sha7') and fail[0]:
                    raise OSError('rate limited')
                return yaml
            return json.dumps(dict(full_name='test/skills', default_branch='main', id=7))

        fail = [True]
        with patch.object(evidence, 'document', side_effect=document), patch.object(
                evidence, 'skill_index', return_value=paths) as index:
            first = []
            with self.assertRaises(OSError):
                for key, _ in evidence.skill_files(item, 'test/skills', time.monotonic() + 90):
                    first.append(key)
            self.assertGreater(len(first), 6)
            item = json.loads(json.dumps(item))
            fail[0] = False
            second = list(evidence.skill_files(item, 'test/skills', time.monotonic() + 90))
            self.assertEqual(len(set(first) | {key for key, _ in second}), 11)
            self.assertEqual(index.call_count, 1)

    def test_news_batch_can_write_twelve_articles(self):
        now = datetime(2026, 11, 25, tzinfo=editor.DATE_ZONE)
        items, articles = {}, []
        for i in range(12):
            key = str(i)
            items[key] = dict(title=f'Source {i}', url=f'https://example.org/{i}', status='pending',
                              category='coding', summary='New release', published='2026-10-01T00:00:00Z')
            articles.append(dict(slug=f'article-{i}', itemIds=[key], body='Body', tags=['test'],
                                 type='news', version='unknown'))
        selected = editor.choose('news', items, now, strategy={'candidate_limit': 18})
        self.assertEqual(len(selected), 12)
        with tempfile.TemporaryDirectory() as directory, patch.object(editor, 'Path', return_value=Path(directory)), patch.object(
                editor, 'metadata'), patch.object(editor, 'resource_context', return_value=[]):
            (Path(directory) / 'news').mkdir()
            editor.write_articles(dict(articles=articles, skipped=[]), 'news', selected, now)
            self.assertEqual(len(list(Path(directory).rglob('*.md'))), 12)

    def test_manifest_version_updates_original_resource(self):
        day = '2026-11-25'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalogue = root / 'catalogue'
            queue = root / 'queue.json'
            with patch.multiple(ingest, DIRECTORY=catalogue, STATE=queue,
                                resource_context=lambda: [json.loads(path.read_text()) for path in catalogue.glob('*.json')]):
                for version, expected in [('1', {'added': 1, 'updated': 0}), ('2', {'added': 0, 'updated': 1})]:
                    site = 'https://example.org/versions/' + version
                    row = ingest.candidate('mcp', 'mcp:org/example', 'Example', site, 'Source summary', site, version=version)
                    state = ingest.load(queue, {})
                    ingest.enqueue(state, row, day)
                    ingest.enqueue(state, dict(row), day)
                    self.assertEqual(len(state['rows']), 1)
                    ingest.save(queue, state)
                    key = next(iter(state['rows']))
                    response = dict(resources=[dict(key=key, zh='示例资源', en='Example resource',
                                                   categoryZh='示例', categoryEn='Example')], skipped=[])
                    self.assertEqual(ingest.publish(response, {key: row}, day), expected)
                entries = list(catalogue.glob('*.json'))
                self.assertEqual(len(entries), 1)
                self.assertEqual(json.loads(entries[0].read_text())['version'], '2')
