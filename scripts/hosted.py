"""Trusted phase entry points for the GitHub-hosted editorial run."""
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta
from decimal import Decimal
from pathlib import Path
from urllib.parse import urlsplit

from collect import canonical, collect, load, save
from discover import discovery
from evidence import enrich
from resource_editor import resource_context
import resource_ingest
import operations_queue
import original
import editorial
from editor import ITEMS, DATE_ZONE, RUN_BUDGET, choose, evidence_revision, metadata, output_schema, sync, write_articles
from model_cost import configured_price, event_usage, worst_case
from release import PROBE_HEADERS, probe

WORK = Path(os.environ.get('RUNNER_TEMP', '.venture-runtime')) / 'venture'
STATE = Path('.venture-runtime')
BATCH = WORK / 'batch.json'
MODEL = WORK / 'model'
REPOSITORY = Path.cwd()
SMOKE_MARKER = 'venture-tool-ok'
MODEL_TIMEOUT = 240
EDIT_WINDOW = 750
BATCH_SLOTS = EDIT_WINDOW // MODEL_TIMEOUT


def number(name, default, minimum, maximum):
    value = int(os.environ.get(name) or default)
    if not minimum <= value <= maximum:
        raise ValueError(f'{name} must be between {minimum} and {maximum}')
    return value


def cost_allows(root, day, tokens, price, reserved_calls):
    limit = os.getenv('VENTURE_DAILY_COST_LIMIT')
    if not limit:
        return True
    currency = os.getenv('VENTURE_COST_CURRENCY')
    if root is None or price is None or price['currency'] != currency or not (
        price['cache_in_input'] and price['reasoning_in_output']
    ):
        return False
    spent = Decimal(0)
    accounted_calls = 0
    for file in (root / 'operations' / day).glob('*.json'):
        receipt = load(file, {}).get('model')
        if not receipt or not receipt.get('sessions'):
            continue
        cost = receipt.get('estimated_cost')
        if not cost or cost['currency'] != currency:
            return False
        spent += Decimal(cost['amount'])
        accounted_calls += receipt['sessions']
    return accounted_calls >= reserved_calls and spent + worst_case(price, tokens) <= Decimal(limit)


def prepare(task, queued=False, excluded=()):
    coverage = operations_queue.public_coverage()
    print('Public coverage:', json.dumps(coverage), flush=True)
    task, days = (task, 7) if queued else operations_queue.select(task)
    if output := os.getenv('GITHUB_OUTPUT'):
        with open(output, 'a') as stream:
            stream.write(f'task={task}\n')
    if task == 'idle':
        operations_queue.record(task, 'SKIPPED')
        return
    from analytics import store
    from analytics_review import strategy
    now = datetime.now(DATE_ZONE)
    day = now.date().isoformat()
    days = number('BACKFILL_DAYS', days, 1, 90) if task == 'backfill' else 7
    resource_task = task.startswith('resource-')
    if task == 'collect':
        collect()
    elif task == 'discover':
        discovery()
    elif task == 'backfill':
        collect(days, refresh=True)
        discovery(days)
    if not queued and task == 'news' and not any(item['status'] == 'pending' for item in load(ITEMS, {}).values()):
        collect()
        discovery()
    if task in original.TYPES:
        original.discover(task, now)
    items, articles = ({}, []) if resource_task else (load(ITEMS, {}), metadata())
    if not resource_task:
        sync(items, articles)
        if task in original.TYPES:
            original.prepare(task, items, now)
            sync(items, articles)
            original.report(task, items, articles)
        save(ITEMS, items)
    if task in ('collect', 'discover'):
        if task == 'discover':
            queued = sorted((key for key, item in items.items()
                             if item['status'] == 'pending' or
                             any(item.get('skill_scan', {}).get(field) for field in ('pending', 'tree_queue'))),
                            key=lambda key: (not bool(items[key].get('research')),
                                              items[key].get('evidence_checked', ''),
                                              items[key].get('source', '')))
            counts = enrich(items, queued, now, limit=10)
            save(ITEMS, items)
            path = BATCH.parent / 'collection.json'
            save(path, {**load(path, {}), **counts})
        counts = load(BATCH.parent / 'collection.json', {})
        operations_queue.record(task, 'COLLECTED' if counts.get('discovered') or counts.get('evidence_succeeded')
                                else 'SOURCE_BLOCKED' if counts.get('failed') and not counts.get('succeeded')
                                else 'NO_NEW_CONTENT')
        return
    slug = 'weekly-' + day if task == 'weekly' else day
    rules = strategy(use_override=os.getenv('VENTURE_STRATEGY_AUTO_UPDATE') == 'true')
    review_strategy = {'reader_review': rules['reader_review']}
    existing_articles = sorted(articles, key=lambda row: row.get('published', ''), reverse=True)
    existing_articles = [{key: row[key] for key in ('slug', 'titleZh', 'titleEn', 'sources') if key in row}
                         for row in existing_articles[:80]]
    eligible = {key: item for key, item in items.items() if key not in excluded} if excluded else items
    candidates = (resource_ingest.prepare(task, os.getenv('RESOURCE_TYPE') or 'all', day, capacity=12 if queued else 12 * BATCH_SLOTS, coverage=coverage.get('resources'), excluded=excluded)
                  if resource_task else choose(task, eligible, now, days if task in ('weekly', 'backfill') else 2, rules))
    if task in ('news', 'backfill'):
        counts = enrich(items, candidates, now, limit=10)
        path = WORK / 'collection.json'
        save(path, {**load(path, {}), **counts})
        save(ITEMS, items)
        eligible = {key: item for key, item in items.items() if key not in excluded} if excluded else items
        candidates = choose(task, eligible, now, days if task == 'backfill' else 2, rules)
    if task != 'smoke-test' and (not candidates or (
        task in ('daily', 'weekly') and any(
            article['collection'] == 'daily' and article['slug'] == slug for article in articles
        )
    )):
        if resource_task:
            stats = resource_ingest.statistics(day)
            print('Resource queue:', json.dumps(stats), flush=True)
            result = ('COLLECTED' if task == 'resource-discover' and stats['queued']
                      else 'BACKLOG' if stats['queued'] else 'NO_NEW_CONTENT')
        else:
            result = 'BACKLOG' if task in ('news', 'backfill') and any(
                item['status'] == 'pending' for item in items.values()) else 'NO_NEW_CONTENT'
        operations_queue.record(task, result)
        print('No eligible editorial batch')
        return

    if queued:
        unlimited = os.getenv('VENTURE_DAILY_TOKEN_LIMIT') == 'unlimited'
        cost_limited = bool(os.getenv('VENTURE_DAILY_COST_LIMIT'))
        if task in ('news', 'backfill') and (not unlimited or cost_limited):
            # Leave room for Codex instructions and output in the per-call reservation.
            selected = {}
            size = 0
            for key, candidate in candidates.items():
                candidate_size = len(json.dumps(candidate, ensure_ascii=False).encode())
                if selected and (len(selected) >= 6 or size + candidate_size > 14000):
                    continue
                selected[key] = candidate
                size += candidate_size
            candidates = selected
        profiles = resource_context() if task in ('news', 'backfill') else []
        context = [{field: row[field] for field in ('id', 'name', 'site')}
                   for row in profiles if any(
                       row['site'] == item['url'] or
                       (row.get('repository') and row['repository'] ==
                        item.get('discovery', {}).get('upstream')) for item in candidates.values())]
        save(BATCH, dict(task=task, date=day, now=now.isoformat(timespec='seconds'),
                         reservation=RUN_BUDGET, unlimited=unlimited, enforce_cost_limit=cost_limited,
                         selectionVersion=3, reviewStrategy=review_strategy, existingArticles=existing_articles,
                         batches=[dict(candidates=candidates, existingResources=context)]))
        return

    ledger_path = STATE / 'usage.json'
    ledger = load(ledger_path, {})
    for value in ledger.values():
        value.pop('usage', None)
    cutoff = now.date().toordinal() - 31
    ledger = {key: value for key, value in ledger.items()
              if datetime.fromisoformat(key).date().toordinal() >= cutoff}
    usage = ledger.setdefault(day, {'tokens': 0, 'calls': 0})
    unlimited = os.environ.get('VENTURE_DAILY_TOKEN_LIMIT') == 'unlimited'
    daily_tokens = None if unlimited else number('VENTURE_DAILY_TOKEN_LIMIT', 100000, 0, 10000000)
    reserved = 40000 if task == 'smoke-test' else RUN_BUDGET
    model = (os.getenv('CODEX_ADVANCED_MODEL') if task == 'weekly' else None) or os.getenv('CODEX_MODEL')
    price = configured_price('venture', model, day)
    root = store()
    slots = BATCH_SLOTS if resource_task else 1
    remaining = dict(items)
    batches = []
    profiles = resource_context() if not resource_task and task in ('news', 'backfill') else []
    for index in range(slots):
        if resource_task:
            selected = dict(list(candidates.items())[index * 12:(index + 1) * 12])
        elif index:
            selected = choose(task, remaining, now, days, rules)
        else:
            selected = candidates
        if not selected and task != 'smoke-test':
            break
        if daily_tokens is not None and usage['tokens'] + (index + 1) * reserved > daily_tokens:
            print('Insufficient daily model allowance for another batch')
            if task == 'smoke-test':
                raise RuntimeError('Smoke test requires sufficient daily model allowance')
            break
        if not cost_allows(root, day, (index + 1) * reserved, price, usage['calls']):
            print('Configured cost allowance cannot reserve another batch')
            break
        context = [{field: row[field] for field in ('id', 'name', 'site')}
                   for row in profiles if any(
                       row['site'] == item['url'] or
                       (row.get('repository') and row['repository'] ==
                        item.get('discovery', {}).get('upstream')) for item in selected.values())]
        batches.append(dict(candidates=selected, existingResources=context))
        for key in selected:
            remaining.pop(key, None)

    if not batches:
        operations_queue.record(task, 'BUDGET_BLOCKED')
        return
    usage['calls'] += len(batches)
    usage['tokens'] += reserved * len(batches)
    save(ledger_path, ledger)
    save(BATCH, dict(task=task, date=day, now=now.isoformat(timespec='seconds'),
                     reservation=reserved, unlimited=unlimited,
                     selectionVersion=3, reviewStrategy=review_strategy, existingArticles=existing_articles,
                     enforce_cost_limit=bool(os.getenv('VENTURE_DAILY_COST_LIMIT')), batches=batches,
                     candidates=batches[0]['candidates']))


def config(smoke, instructions, directory=None, *, yolo=False):
    required = ('CODEX_BASE_URL', 'CODEX_MODEL', 'CODEX_API_KEY')
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise ValueError('Missing GitHub Actions configuration: ' + ', '.join(missing))
    url = os.environ['CODEX_BASE_URL']
    parts = urlsplit(url)
    if (parts.scheme != 'https' or not parts.hostname or parts.username or parts.password
            or parts.query or parts.fragment or parts.hostname.lower() == 'api.openai.com'):
        raise ValueError('CODEX_BASE_URL must be a third-party HTTPS API base URL')
    advanced = load(BATCH, {})['task'] == 'weekly' and os.environ.get('CODEX_ADVANCED_MODEL')
    model = os.environ.get('CODEX_ADVANCED_MODEL' if advanced else 'CODEX_MODEL', '')
    effort = (os.environ.get('CODEX_ADVANCED_REASONING_EFFORT' if advanced else
                             'CODEX_REASONING_EFFORT') or 'low')
    if not model or effort not in ('none', 'minimal', 'low', 'medium', 'high', 'xhigh'):
        raise ValueError('Invalid Codex model or reasoning effort')
    home = directory if directory is not None else Path.home() / '.codex'
    home.mkdir(mode=0o700, exist_ok=True)
    if (home / 'auth.json').exists():
        raise RuntimeError('Hosted Codex requires a fresh home without auth.json')
    config_file = home / 'config.toml'
    plugin_config = 'plugins = false\nremote_plugin = false\nskill_search = false\n' if yolo else ''
    config_file.write_text(f'''model = {json.dumps(model)}
model_provider = "venture"
model_reasoning_effort = {json.dumps(effort)}
model_instructions_file = {json.dumps(str(instructions))}
approval_policy = "never"
sandbox_mode = "workspace-write"
web_search = "disabled"

[analytics]
enabled = false

[features]
shell_tool = false
shell_snapshot = false
{plugin_config}
[sandbox_workspace_write]
network_access = false

[shell_environment_policy]
inherit = "none"
ignore_default_excludes = false

[model_providers.venture]
name = "Third Party API"
base_url = {json.dumps(url.rstrip('/'))}
env_key = "CODEX_API_KEY"
wire_api = "responses"
requires_openai_auth = false
supports_websockets = false
request_max_retries = 0
stream_max_retries = 0
''')
    if smoke:
        with config_file.open('a') as handle:
            handle.write(f'\n[mcp_servers.venture_smoke]\ncommand = {json.dumps(sys.executable)}\n'
                         f'args = [{json.dumps(str(REPOSITORY / "scripts/hosted.py"))}, "smoke-tool"]\n'
                         'required = true\n\n[mcp_servers.venture_smoke.tools.check]\n'
                         'approval_mode = "approve"\n')
    config_file.chmod(0o600)


def invoke(*, yolo=False):
    batch = load(BATCH, {})
    smoke = batch['task'] == 'smoke-test'
    MODEL.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    receipts = []
    responses = []
    failure = None
    for part in batch['batches']:
        receipt = {'provider': 'venture', 'status': 'failed', 'usage': None, 'billed_cost': None,
                   'estimated_cost': None, 'sessions': 0}
        receipts.append(receipt)
        try:
            response = run_model({**batch, **part}, smoke, receipt, yolo=yolo)
            responses.append(response)
            receipt['status'] = 'success'
        except (RuntimeError, OSError, ValueError) as error:
            failure = error
            print(f'Model batch {len(receipts)} failed: {error}', flush=True)
            responses.append(None)
        if time.monotonic() - started > EDIT_WINDOW - MODEL_TIMEOUT:
            break
    usage = None
    charged = [row for row in receipts if row['sessions']]
    if charged and all(row['usage'] is not None for row in charged):
        fields = set.intersection(*(set(row['usage']) for row in charged))
        usage = {field: sum(row['usage'][field] for row in charged) for field in fields}
        print(f"Observed model tokens: {usage['input_tokens']} input, {usage['output_tokens']} output")
    completed = sum(response is not None for response in responses)
    sessions = sum(row['sessions'] for row in charged)
    print(f'Model sessions: {sessions} attempted, {completed} batches completed')
    save(MODEL / 'receipt.json', {**receipts[0], 'usage': usage, 'sessions': sessions,
                                'status': 'partial' if failure and completed else 'failed' if failure else 'success',
                                'batches': receipts, 'duration_seconds': round(time.monotonic() - started, 3)})
    if failure and not completed:
        raise failure
    if not smoke:
        save(MODEL / 'response.json', responses)


def run_model(batch, smoke, receipt, *, yolo=False):
    resource = batch['task'].startswith('resource-')
    if smoke or resource:
        return model_call(batch, smoke, receipt, yolo=yolo)

    stages = []
    receipt['stages'] = stages

    def run(stage, schema, payload):
        stage_receipt = {'stage': stage, 'sessions': 0, 'usage': None}
        stages.append(stage_receipt)
        try:
            return model_call(batch, False, stage_receipt, yolo=yolo, stage=stage, schema_override=schema,
                              payload_override=payload)
        finally:
            stage_receipt['candidate_count'] = len(payload.get('candidates', {}))
            attempted = [row for row in stages if row['sessions']]
            receipt['sessions'] = len(attempted)
            receipt.update({key: stage_receipt[key] for key in ('model', 'effort') if key in stage_receipt})
            if attempted and all(row['usage'] is not None for row in attempted):
                fields = set.intersection(*(set(row['usage']) for row in attempted))
                receipt['usage'] = {field: sum(row['usage'][field] for row in attempted) for field in fields}
            else:
                receipt['usage'] = None
            usage = receipt['usage']
            if ((not batch['unlimited'] or batch['enforce_cost_limit']) and usage and
                    usage['input_tokens'] + usage['output_tokens'] > batch['reservation']):
                raise RuntimeError('Editorial stages exceeded the batch reservation')

    candidates = batch['candidates']
    existing = batch.get('existingArticles', [])
    traced = batch.get('selectionVersion', 0) >= 3
    if traced:
        from growth import relevant_coverage
        existing = relevant_coverage(existing, candidates)
    pitch_fields = editorial.PITCH['properties']['pitches']['items']['properties']
    candidate_id = dict(type='string', enum=list(candidates))
    selection_fields = {'pitches': dict(type='array', items=editorial.obj(
        **(pitch_fields | {'id': candidate_id})
    ))}
    reasons = dict(type='array', items=editorial.obj(id=candidate_id, reason=dict(type='string')))
    if traced:
        selection_fields['rejections'] = reasons
    selection_schema = editorial.obj(**selection_fields)
    selection = run('editorial-selection', selection_schema, dict(candidates=candidates, existingArticles=existing))
    if traced:
        reasons['maxItems'] = len(candidates)
    if not editorial.conforms(selection, selection_schema):
        receipt['selection_response'] = selection
        raise ValueError('Invalid editorial selection schema')
    rejections = selection.pop('rejections', [])
    if traced:
        validate_candidate_dispositions(candidates, selection['pitches'], rejections)
        receipt['candidate_dispositions'] = {'pitches': selection['pitches'], 'rejections': rejections}
    if not editorial.conforms(selection, editorial.PITCH):
        raise ValueError('Invalid editorial selection')
    pitches = {row['id']: row for row in selection['pitches']}
    if not pitches.keys() <= candidates.keys():
        raise ValueError('Invalid editorial candidate IDs')
    selection['pitches'] = list(pitches.values())
    if any(not value.strip() for row in pitches.values() for field, value in row.items() if field not in ('researchGap', 'researchUrl')):
        raise ValueError('Incomplete editorial pitch')
    pitches = {key: row for key, row in pitches.items() if not row['researchGap']}
    if not pitches:
        return dict(draft={'articles': [], 'skipped': []}, review={'reviews': []}, selection=selection)
    selected = {key: candidates[key] for key in pitches}
    schema = output_schema(selected)
    if traced:
        schema = editorial.obj(articles=schema['properties']['articles'], unwritten=reasons)
    draft = run('editor', schema, dict(candidates=selected, pitches=pitches,
                                      existingResources=batch['existingResources']))
    if traced:
        if not editorial.conforms(draft, schema):
            raise ValueError('Invalid traced draft')
        unwritten = draft.pop('unwritten')
        draft['skipped'] = []
        written = {key for article in draft['articles'] for key in article['itemIds']}
        validate_candidate_dispositions(selected, [{'id': key} for key in written], unwritten)
        receipt['candidate_dispositions']['unwritten'] = unwritten
    if not editorial.conforms(draft, output_schema(selected)):
        raise ValueError('Invalid draft')
    review = run('reader-review', editorial.REVIEW, dict(articles=draft['articles'], candidates=selected,
                                                       existingArticles=existing)) if draft['articles'] else {'reviews': []}
    accepted, _ = editorial.decisions(draft, review, batch.get('reviewStrategy', {}))
    if traced:
        receipt['candidate_dispositions']['reviews'] = review['reviews']
        receipt['candidate_dispositions']['accepted'] = [article['slug'] for article in accepted]
    return dict(draft=draft, review=review, selection=selection)


def validate_candidate_dispositions(candidates, positive, negative):
    ids = [row['id'] for row in positive + negative]
    if len(ids) != len(candidates) or set(ids) != set(candidates):
        raise ValueError('Each candidate needs exactly one disposition')
    if any(not row['reason'].strip() for row in negative):
        raise ValueError('Missing candidate disposition reason')


def model_call(batch, smoke, receipt, *, yolo=False, stage=None, schema_override=None, payload_override=None):
    with tempfile.TemporaryDirectory(prefix='venture-edit-') as directory:
        workspace = Path(directory)
        schema, result = workspace / 'schema.json', workspace / 'result.json'
        instructions = workspace / 'instructions.txt'
        instructions.write_text(
            'Call the fixed venture_smoke check tool and return its marker as JSON.' if smoke else
            (REPOSITORY / (f'ops/{stage}.md' if stage else
                           'ops/resource-editor.md' if batch['task'].startswith('resource-') else 'ops/editor.md')).read_text()
        )
        receipt['sessions'] = 0
        config(smoke, instructions, workspace / '.codex', yolo=yolo)
        advanced = batch['task'] == 'weekly' and os.getenv('CODEX_ADVANCED_MODEL')
        receipt['model'] = os.environ['CODEX_ADVANCED_MODEL' if advanced else 'CODEX_MODEL']
        receipt['effort'] = os.getenv('CODEX_ADVANCED_REASONING_EFFORT' if advanced else
                                     'CODEX_REASONING_EFFORT') or 'low'
        receipt['sessions'] = 1
        payload = {key: batch[key] for key in ('date', 'candidates', 'existingResources')}
        if batch['task'].startswith('resource-'):
            payload = dict(candidates=resource_ingest.editorial_input(batch['candidates']))
        if payload_override is not None:
            payload = {'date': batch['date'], **payload_override}
        prompt = json.dumps(dict(mode=batch['task'], **payload), ensure_ascii=False, separators=(',', ':'))
        print(f'Editorial stdin: {len(prompt.encode())} bytes for {len(batch["candidates"])} candidates')
        schema_data = resource_ingest.SCHEMA if batch['task'].startswith('resource-') else output_schema(batch['candidates'])
        if schema_override is not None:
            schema_data = schema_override
        if smoke:
            schema_data = dict(type='object', properties={'marker': {'type': 'string'}},
                               required=['marker'], additionalProperties=False)
            prompt = "Call the venture_smoke check tool once and return its output text as marker."
        save(schema, schema_data)
        sandbox_args = ['--sandbox', 'workspace-write' if smoke else 'read-only']
        if yolo and not smoke:
            sandbox_args = ['--dangerously-bypass-approvals-and-sandbox']
        command = [
            'codex', 'exec', '--skip-git-repo-check', '--ephemeral', '--json',
            *sandbox_args,
            '--output-schema', str(schema), '-o', str(result), '-',
        ]
        environment = {name: os.environ[name] for name in
                       ('PATH', 'HOME', 'LANG', 'CODEX_API_KEY') if name in os.environ}
        environment['CODEX_HOME'] = str(workspace / '.codex')
        key = environment['CODEX_API_KEY']
        with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              text=True, cwd=workspace, env=environment, start_new_session=True) as process:
            timed_out = False
            try:
                events_text, errors = process.communicate(prompt, timeout=MODEL_TIMEOUT)
            except subprocess.TimeoutExpired:
                timed_out = True
                os.killpg(process.pid, signal.SIGKILL)
                events_text, errors = process.communicate()
        redacted_events = events_text.replace(key, '[REDACTED]')
        events = []
        for line in redacted_events.splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                continue
        usage = event_usage(events)
        receipt['usage'] = usage
        if timed_out or process.returncode or not result.is_file() or usage is None:
            raise RuntimeError(f'Codex failed (exit={process.returncode}, timeout={timed_out})')
        if (not batch['unlimited'] or batch['enforce_cost_limit']) and usage['input_tokens'] + usage['output_tokens'] > batch['reservation']:
            raise RuntimeError('Codex exceeded the reserved token budget')
        if result.stat().st_size > 160_000:
            raise ValueError('Model result exceeds file size limit')
        result_text = result.read_text()
        if key in result_text or key in json.dumps(json.loads(result_text), ensure_ascii=False):
            raise ValueError('Model result contains a credential')
        response = json.loads(result_text)
        if smoke:
            tool_ok = any(item.get('type') == 'mcp_tool_call' and item.get('server') == 'venture_smoke'
                          and item.get('tool') == 'check' and item.get('status') == 'completed'
                          and SMOKE_MARKER in json.dumps(item.get('result'))
                          for event in events if event.get('type') == 'item.completed'
                          for item in [event.get('item', {})])
            if not tool_ok or response != {'marker': SMOKE_MARKER}:
                raise RuntimeError('Responses API smoke test did not complete the tool round trip')
        return response


def smoke_tool():
    """A stdio MCP server with one fixed response and no command or file access."""
    for line in sys.stdin:
        message = json.loads(line)
        if 'id' not in message:
            continue
        method = message.get('method')
        response = dict(jsonrpc='2.0', id=message['id'])
        if method == 'initialize':
            response['result'] = dict(protocolVersion=message['params']['protocolVersion'],
                                      capabilities={'tools': {}},
                                      serverInfo={'name': 'venture-smoke', 'version': '1'})
        elif method == 'tools/list':
            response['result'] = {'tools': [{'name': 'check', 'description': 'Return a fixed marker',
                                            'inputSchema': {'type': 'object', 'properties': {},
                                                            'additionalProperties': False}}]}
        elif method == 'tools/call' and message['params']['name'] == 'check':
            response['result'] = {'content': [{'type': 'text', 'text': SMOKE_MARKER}]}
        elif method == 'ping':
            response['result'] = {}
        else:
            response['error'] = {'code': -32601, 'message': 'Method not found'}
        print(json.dumps(response), flush=True)


def as_log(value):
    return json.dumps(value, ensure_ascii=True)


def accept():
    batch = load(BATCH, {})
    model = WORK / 'result'
    result = model / 'response.json'
    if not result.is_file() or result.is_symlink() or result.stat().st_size > 200_000 * len(batch['batches']):
        raise ValueError('Missing or invalid model result')
    results = load(result, [])
    if type(results) is not list or not 0 < len(results) <= len(batch['batches']):
        raise ValueError('Invalid batch results')
    routes, counts = [], {'added': 0, 'updated': 0, 'invalid': 0}
    directories = set()
    for part, response in zip(batch['batches'], results):
        if response is None:
            continue
        if batch['task'].startswith('resource-'):
            stats = resource_ingest.publish(response, part['candidates'], batch['date'])
            for key in counts:
                counts[key] += stats[key]
            directories.update(row['type'] for row in part['candidates'].values())
        else:
            if type(response) is not dict or set(response) != {'draft', 'review', 'selection'}:
                raise ValueError('Missing independently reviewed editorial result')
            selected = response['selection']
            if batch.get('selectionVersion', 0) < 2:
                selected = {'pitches': [dict(audience='adjacent', researchGap='', researchUrl='') | row
                                        for row in selected['pitches']]}
                response['review'] = {'reviews': [dict(audience='adjacent') | row
                                                  for row in response['review']['reviews']]}
            if not editorial.conforms(selected, editorial.PITCH):
                raise ValueError('Invalid editorial selection receipt')
            pitches = {row['id'] for row in selected['pitches']}
            if (len(pitches) != len(selected['pitches']) or not pitches <= part['candidates'].keys()
                    or any(not value.strip() for row in selected['pitches'] for field, value in row.items()
                           if field not in ('researchGap', 'researchUrl'))):
                raise ValueError('Invalid selected candidate pitches')
            research = {row['id']: row for row in selected['pitches'] if row['researchGap']}
            pitches -= research.keys()
            candidates = {key: part['candidates'][key] for key in pitches}
            draft = response['draft']
            if not editorial.conforms(draft, output_schema(candidates)) or any(
                not set(article['itemIds']) <= pitches for article in draft['articles']
            ) or not set(draft['skipped']) <= pitches:
                raise ValueError('Draft contains unselected evidence')
            accepted, ratings = editorial.decisions(draft, response['review'], batch.get('reviewStrategy', {}))
            routes.extend(accept_articles({**batch, **part, 'candidates': candidates},
                                          dict(articles=accepted, skipped=[]), ratings))
            items = load(ITEMS, {})
            for key, candidate in part['candidates'].items():
                if key in items:
                    if key in research and items[key]['status'] == 'pending':
                        row = research[key]
                        topic = items[key].setdefault('research', {})
                        topic.update(gap=row['researchGap'], angle=row['angle'], audience=row['audience'])
                        topic.setdefault('opened', batch['date'])
                        if row['researchUrl']:
                            try:
                                topic['url'] = canonical(row['researchUrl'])
                            except ValueError:
                                pass
                    elif items[key]['status'] != 'pending':
                        items[key].pop('research', None)
                    items[key].setdefault('editorial_attempts', {})[batch['task']] = evidence_revision(candidate)
            save(ITEMS, items)
    save(WORK / 'routes.json', routes)
    save(WORK / 'resources-published.json', counts)
    print('Resource decisions:', json.dumps(counts), flush=True)
    save(WORK / 'resource-routes.json', [f'topics/{kind}/index.json' for kind in sorted(directories)])


def accept_articles(batch, response, ratings):
    if type(response) is not dict or set(response) != {'articles', 'skipped'}:
        raise ValueError('Invalid editorial response')
    if type(response['articles']) is not list or not string_list(response['skipped'], len(batch['candidates']), 64):
        raise ValueError('Invalid editorial lists')
    for article in response['articles']:
        fields = output_schema()['properties']['articles']['items']['properties']
        if type(article) is not dict or set(article) != set(fields):
            raise ValueError('Invalid article fields')
        for name, field in fields.items():
            value = article[name]
            if field['type'] == 'string':
                if not isinstance(value, str) or not value.strip() or len(value) > (
                    12000 if name == 'body' else 600
                ):
                    raise ValueError(f'Invalid field {name}')
                if name != 'body' and re.search(r'[<>\x00-\x1f]', value):
                    raise ValueError(f'Unsupported metadata characters in {name}')
            elif name == 'blocks':
                continue  # Validated by write_articles in both publishing paths.
            elif not string_list(value, 8, 64):
                raise ValueError(f'Invalid array {name}')
    before = {(article['collection'], article['slug']): article for article in metadata()}
    now = datetime.fromisoformat(batch['now'])
    if now.date().isoformat() != batch['date']:
        raise ValueError('Batch date is invalid')
    if batch['task'] in ('daily', 'weekly'):
        for article in response['articles']:
            original_slug = article['slug']
            article['slug'] = ('weekly-' if batch['task'] == 'weekly' else '') + batch['date']
            ratings[article['slug']] = ratings.pop(original_slug)
    skipped = write_articles(response, batch['task'], batch['candidates'], now, ratings=ratings)
    articles = metadata()
    items = load(ITEMS, {})
    sync(items, articles)
    for key in skipped:
        if key in items and items[key]['status'] in ('pending', 'expired'):
            items[key]['status'] = 'skipped'
    save(ITEMS, items)
    routes = [f"{article['collection']}/{article['slug']}/" for article in articles
              if article != before.get((article['collection'], article['slug']))]
    return routes


def finish():
    batch = load(BATCH, {})
    receipt = load(WORK / 'receipt' / 'receipt.json', {})
    if receipt.get('batches') and batch:
        path = STATE / 'usage.json'
        ledger = load(path, {})
        day = ledger.get(batch['date'])
        identity = f"{os.getenv('GITHUB_RUN_ID')}:{os.getenv('GITHUB_RUN_ATTEMPT')}"
        if day is not None and identity not in day.get('settled', []):
            rows = receipt['batches']
            usage = sum(
                (row['usage']['input_tokens'] + row['usage']['output_tokens']
                 if row.get('usage') is not None else batch['reservation'])
                for row in rows if row['sessions']
            )
            day['tokens'] += usage - batch['reservation'] * len(batch['batches'])
            day['calls'] += receipt['sessions'] - len(batch['batches'])
            day.setdefault('settled', []).append(identity)
            save(path, ledger)
    task = os.environ['TASK']
    if task in original.TYPES:
        original.report(task, load(ITEMS, {}), metadata(), receipt)
    if os.getenv('CONTENT_CHANGED') == 'true':
        result = 'PUBLISHED' if os.getenv('PRODUCTION_RESULT') == 'success' else 'DEPLOY_FAILED'
    elif task == 'smoke-test':
        result = 'SKIPPED'
    else:
        result = 'BACKLOG'
    operations_queue.record(task, result)


def string_list(value, count, length):
    return type(value) is list and len(value) <= count and all(
        isinstance(item, str) and 0 < len(item) <= length for item in value
    )


def health(wait=False):
    from urllib.request import Request, urlopen

    base = 'https://codex-venture.com'
    release = Path('dist/release.txt').read_text().strip()
    routes = load(WORK / 'routes.json', [])
    resource_routes = load(WORK / 'resource-routes.json', [])
    for attempt in range(24 if wait else 1):
        try:
            probe(base, release)
            if Path('dist/coverage.json').exists():
                request = Request(f'{base}/coverage.json?release={release}', headers=PROBE_HEADERS)
                with urlopen(request, timeout=8) as response:
                    coverage = json.load(response)
                if coverage != load(Path('dist/coverage.json'), {}):
                    raise RuntimeError('Public coverage differs from the built inventory')
            for route in routes:
                request = Request(f'{base}/{route}?release={release}', headers=PROBE_HEADERS)
                with urlopen(request, timeout=8) as response:
                    page = response.read(2_000_000)
                expected = (Path('dist') / route / 'index.html').read_bytes()
                article = rb'<article\b[^>]*\bdata-pagefind-body[^>]*>.*?</article>'
                deployed = re.search(article, page, re.DOTALL)
                built = re.search(article, expected, re.DOTALL)
                if not deployed or not built or deployed.group() != built.group():
                    raise RuntimeError(f'{route} differs from the built article')
            for route in resource_routes:
                request = Request(f'{base}/{route}?release={release}', headers=PROBE_HEADERS)
                with urlopen(request, timeout=8) as response:
                    deployed = json.load(response)
                if deployed != load(Path('dist') / route, []):
                    raise RuntimeError(f'{route} differs from the built resource index')
            print(f'Public release {release} verified, {len(routes)} new articles, '
                  f'{len(resource_routes)} changed resource directories')
            return
        except (OSError, RuntimeError) as error:
            if not wait or attempt == 23:
                raise
            print(f'Waiting for Cloudflare deployment: {error}', flush=True)
            time.sleep(20)


if __name__ == '__main__':
    actions = {'prepare': prepare, 'invoke': invoke, 'accept': accept,
               'health': health, 'smoke-tool': smoke_tool, 'finish': finish}
    command, *arguments = sys.argv[1:]
    actions[command](*arguments)
