import os
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, 'scripts')
import operations_queue as queue


class OperationsQueue(unittest.TestCase):
    def test_interrupted_work_is_recovered_from_the_due_time(self):
        with tempfile.TemporaryDirectory() as temporary, patch.object(
            queue, 'PATH', Path(temporary) / 'queue.json'
        ), patch.object(queue, 'datetime', wraps=datetime) as clock:
            clock.now.return_value = datetime(2026, 11, 25, 12, tzinfo=queue.DATE_ZONE)
            self.assertEqual(queue.select('cycle'), ('collect', 7))
            self.assertEqual(queue.load(queue.PATH, {})['collect']['result'], 'SKIPPED')
            self.assertEqual(queue.select('cycle'), ('discover', 7))
            clock.now.return_value = datetime(2026, 11, 25, 13, tzinfo=queue.DATE_ZONE)
            queue.save(queue.PATH, {**queue.load(queue.PATH, {}), **{
                task: {'due': '2026-11-26T12:00:00+08:00'}
                for task in queue.INTERVALS if task not in ('collect', 'discover')
            }})
            self.assertEqual(queue.select('cycle'), ('collect', 7))

    def test_backfill_advances_only_after_a_completed_window(self):
        with tempfile.TemporaryDirectory() as temporary, patch.object(
            queue, 'PATH', Path(temporary) / 'queue.json'
        ), patch.dict(os.environ, {'BACKFILL_DAYS': ''}):
            self.assertEqual(queue.select('backfill'), ('backfill', 7))
            queue.record('backfill', 'BUDGET_BLOCKED')
            self.assertEqual(queue.select('backfill'), ('backfill', 7))
            queue.record('backfill', 'PUBLISHED')
            self.assertEqual(queue.select('backfill'), ('backfill', 30))
            queue.record('backfill', 'NO_NEW_CONTENT')
            self.assertEqual(queue.select('backfill'), ('backfill', 90))
