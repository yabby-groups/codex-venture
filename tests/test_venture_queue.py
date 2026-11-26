import os
import sys
import tempfile
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import collection_budget
import venture_queue as queue


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / 'queue.sqlite'
        queue.initialize(self.path)
        self.db = queue.connect(self.path)
        self.addCleanup(self.db.close)
        queue.store(self.db, 'paused', False)

    def test_claim_is_atomic_and_recovers_unstarted_work(self):
        queue.enqueue(self.db, 'collector', 'news', 'news-one')
        queue.enqueue(self.db, 'collector', 'news', 'news-one')

        def claim(worker):
            with queue.connect(self.path) as db:
                return queue.claim(db, 'collector', str(worker))

        with ThreadPoolExecutor(2) as pool:
            self.assertEqual(sum(row is not None for row in pool.map(claim, range(2))), 1)
        self.db.execute('UPDATE tasks SET lease_expires_at=0')
        self.assertEqual(claim('replacement')['dedupe_key'], 'news-one')

    def test_inherited_tokens_and_parallel_cost_reservation(self):
        self.db.execute('INSERT INTO legacy_usage VALUES (?,?)', ('day', '{"tokens": 20, "calls": 1}'))

        def reserve(task):
            with queue.connect(self.path) as db, queue.transaction(db):
                return queue.reserve(db, task, 'day', 60, Decimal('0.4'), 120,
                                     Decimal('1.0'), Decimal('0.5'))

        with ThreadPoolExecutor(2) as pool:
            self.assertEqual(sum(pool.map(reserve, (1, 2))), 1)

    def test_unknown_usage_blocks_replay(self):
        queue.enqueue(self.db, 'editor', 'edit', 'news-one')
        row = queue.claim(self.db, 'editor', 'editor')
        with queue.transaction(self.db):
            self.assertTrue(queue.reserve(self.db, row['id'], 'day', 100, None, 100, None))
        self.db.execute('UPDATE tasks SET lease_expires_at=0')
        self.assertIsNone(queue.claim(self.db, 'editor', 'replacement'))
        self.assertEqual(self.db.execute('SELECT status FROM tasks').fetchone()[0], 'blocked')

    def test_regular_tasks_age_past_repeated_high_priority_work(self):
        queue.enqueue(self.db, 'collector', 'resource-sync', 'resources', priority=5)
        self.db.execute('UPDATE tasks SET available_at=?', (time.time() - 7200,))
        queue.enqueue(self.db, 'collector', 'collect', 'collect', priority=25)
        self.assertEqual(queue.claim(self.db, 'collector', 'worker')['type'], 'resource-sync')

    def test_resource_lane_preserves_news_capacity(self):
        path = Path(self.directory.name) / 'requests.json'
        host = 'example.test'
        with patch.object(collection_budget, 'PATH', path), patch.dict(collection_budget.LIMITS, {host: (3, 12)}):
            with patch.dict(os.environ, {'VENTURE_COLLECTION_LANE': 'resource'}):
                collection_budget.reserve(host)
                collection_budget.reserve(host)
                with self.assertRaisesRegex(collection_budget.CollectionPaused, 'local hourly'):
                    collection_budget.reserve(host)
            with patch.dict(os.environ, {'VENTURE_COLLECTION_LANE': 'news'}):
                collection_budget.reserve(host)
                with self.assertRaises(collection_budget.CollectionPaused):
                    collection_budget.reserve(host)
