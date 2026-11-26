"""SQLite task ownership and model accounting."""
import json
import sqlite3
import time
from contextlib import contextmanager
from decimal import Decimal

LEASE = 90
SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY, type TEXT NOT NULL, role TEXT NOT NULL,
    priority INTEGER NOT NULL, status TEXT NOT NULL, dedupe_key TEXT UNIQUE NOT NULL,
    payload TEXT NOT NULL, scheduled_at REAL NOT NULL, available_at REAL NOT NULL,
    attempts INTEGER NOT NULL DEFAULT 0, lease_owner TEXT, lease_expires_at REAL,
    started_at REAL, finished_at REAL, last_error TEXT, result TEXT,
    created_at REAL NOT NULL, updated_at REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS ready ON tasks(role,status,available_at);
CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS heartbeat (role TEXT PRIMARY KEY, updated_at REAL NOT NULL);
CREATE TABLE IF NOT EXISTS model_usage (
    task INTEGER PRIMARY KEY, day TEXT NOT NULL, tokens INTEGER NOT NULL,
    cost TEXT, receipt TEXT
);
CREATE TABLE IF NOT EXISTS legacy_usage (day TEXT PRIMARY KEY, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS fairness (type TEXT PRIMARY KEY, last_claim REAL NOT NULL);
"""


def connect(path):
    db = sqlite3.connect(path, timeout=15, isolation_level=None)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA busy_timeout=15000')
    return db


def initialize(path):
    with connect(path) as db:
        db.execute('PRAGMA journal_mode=WAL')
        db.executescript(SCHEMA)


@contextmanager
def transaction(db):
    db.execute('BEGIN IMMEDIATE')
    try:
        yield
        db.commit()
    except BaseException:
        db.rollback()
        raise


def setting(db, key, default=None):
    row = db.execute('SELECT value FROM settings WHERE key=?', (key,)).fetchone()
    return json.loads(row[0]) if row else default


def store(db, key, value):
    db.execute('INSERT OR REPLACE INTO settings VALUES (?,?)', (key, json.dumps(value)))


def enqueue(db, role, kind, key, payload=None, priority=10, delay=0):
    now = time.time()
    db.execute("""
        INSERT OR IGNORE INTO tasks
        (type,role,priority,status,dedupe_key,payload,scheduled_at,available_at,created_at,updated_at)
        VALUES (?,?,?,'pending',?,?,?,?,?,?)
    """, (kind, role, priority, key, json.dumps(payload or {}), now, now + delay, now, now))


def recover(db, now):
    db.execute("""
        UPDATE tasks SET status=CASE
            WHEN role='editor' AND EXISTS(SELECT 1 FROM model_usage WHERE task=tasks.id) THEN 'blocked'
            WHEN attempts>=5 THEN 'dead' ELSE 'retry' END,
        lease_owner=NULL,lease_expires_at=NULL,updated_at=?,available_at=?,
        last_error=CASE WHEN role='editor' THEN 'Lease expired. Inspect model reservation before retry.'
                        ELSE 'Worker lease expired' END
        WHERE status='running' AND lease_expires_at<?
    """, (now, now, now))


def claim(db, role, owner):
    now = time.time()
    with transaction(db):
        recover(db, now)
        if setting(db, 'paused', True):
            return None
        row = db.execute("""
            SELECT t.* FROM tasks t LEFT JOIN fairness f ON f.type=t.type
            WHERE role=? AND status IN ('pending','retry') AND available_at<=?
            ORDER BY MIN(priority,30) + MIN(60,(?-available_at)/60)
                     + MIN(30,(?-COALESCE(f.last_claim,0))/60) DESC,
                     scheduled_at,id LIMIT 1
        """, (role, now, now, now)).fetchone()
        if row:
            db.execute("""UPDATE tasks SET status='running', attempts=attempts+1,
                       lease_owner=?,lease_expires_at=?,started_at=?,updated_at=? WHERE id=?""",
                       (owner, now + LEASE, now, now, row['id']))
            db.execute('INSERT OR REPLACE INTO fairness VALUES (?,?)', (row['type'], now))
        return row


def renew(db, task, owner):
    now = time.time()
    return db.execute("""UPDATE tasks SET lease_expires_at=?,updated_at=?
                      WHERE id=? AND lease_owner=? AND lease_expires_at>=?""",
                      (now + LEASE, now, task, owner, now)).rowcount == 1


def finish(db, task, owner, status, result=None, error=None, delay=0):
    now = time.time()
    count = db.execute("""
        UPDATE tasks SET status=?,result=?,last_error=?,available_at=?,updated_at=?,
        finished_at=?,lease_owner=NULL,lease_expires_at=NULL WHERE id=? AND lease_owner=?
    """, (status, json.dumps(result), error, now + delay, now, now, task, owner)).rowcount
    if count != 1:
        raise RuntimeError('Task lease lost')


def reserve(db, task, day, tokens, cost, token_limit, cost_limit, legacy_cost=None):
    """Call in the same write transaction as the check of task ownership."""
    legacy = db.execute('SELECT data FROM legacy_usage WHERE day=?', (day,)).fetchone()
    baseline = json.loads(legacy[0]) if legacy else {}
    rows = db.execute('SELECT tokens,cost FROM model_usage WHERE day=?', (day,)).fetchall()
    if token_limit is not None and baseline.get('tokens', 0) + sum(r[0] for r in rows) + tokens > token_limit:
        return False
    if cost_limit is not None:
        if (baseline.get('calls', 0) and legacy_cost is None) or cost is None or any(r[1] is None for r in rows):
            return False
        if (legacy_cost or Decimal(0)) + sum(Decimal(r[1]) for r in rows) + cost > cost_limit:
            return False
    db.execute('INSERT INTO model_usage VALUES (?,?,?,?,NULL)',
               (task, day, tokens, str(cost) if cost is not None else None))
    return True
