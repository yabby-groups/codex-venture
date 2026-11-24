"""Trusted phase entry points for the GitHub-hosted editorial run."""
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

from collect import collect, load, save
from discover import discovery
from editor import ITEMS, DATE_ZONE, RUN_BUDGET, choose, metadata, output_schema, sync, write_articles
from release import PROBE_HEADERS, probe

WORK = Path(os.environ.get('RUNNER_TEMP', '.venture-runtime')) / 'venture'
STATE = Path('.venture-runtime')
BATCH = WORK / 'batch.json'
MODEL = WORK / 'model'
REPOSITORY = Path.cwd()
SMOKE_MARKER = 'venture-tool-ok'


def number(name, default, minimum, maximum):
    value = int(os.environ.get(name) or default)
    if not minimum <= value <= maximum:
        raise ValueError(f'{name} must be between {minimum} and {maximum}')
    return value


def prepare(task):
    now = datetime.now(DATE_ZONE)
    day = now.date().isoformat()
    days = number('BACKFILL_DAYS', 7, 1, 30) if task == 'backfill' else 7
    if task == 'collect':
        collect()
    elif task == 'discover':
        discovery()
    elif task == 'backfill':
        collect(days, refresh=True)
        discovery(days)
    items, articles = load(ITEMS, {}), metadata()
    sync(items, articles)
    save(ITEMS, items)
    if task in ('collect', 'discover'):
        return
    slug = 'weekly-' + day if task == 'weekly' else day
    candidates = choose(task, items, now, days if task in ('weekly', 'backfill') else 2)
    if task != 'smoke-test' and (not candidates or (
        task in ('daily', 'weekly') and any(
            article['collection'] == 'daily' and article['slug'] == slug for article in articles
        )
    )):
        print('No eligible editorial batch')
        return

    ledger_path = STATE / 'usage.json'
    ledger = load(ledger_path, {})
    cutoff = now.date().toordinal() - 31
    ledger = {key: value for key, value in ledger.items()
              if datetime.fromisoformat(key).date().toordinal() >= cutoff}
    usage = ledger.setdefault(day, {'tokens': 0, 'calls': 0})
    daily_tokens = number('VENTURE_DAILY_TOKEN_LIMIT', 100000, 0, 10000000)
    daily_calls = number('VENTURE_MAX_MODEL_CALLS_PER_DAY', 6, 0, 1000)
    reserved = min(RUN_BUDGET, daily_tokens - usage['tokens'])
    if usage['calls'] >= daily_calls or reserved <= 0:
        print('Daily model budget exhausted')
        return
    usage['calls'] += 1
    usage['tokens'] += reserved
    save(ledger_path, ledger)
    save(BATCH, dict(task=task, date=day, now=now.isoformat(timespec='seconds'),
                     maxArticles=number('VENTURE_MAX_ARTICLES_PER_RUN', 3, 1, 10),
                     reservation=reserved, candidates=candidates))


def config(smoke, instructions):
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
    home = Path.home() / '.codex'
    home.mkdir(mode=0o700, exist_ok=True)
    if (home / 'auth.json').exists():
        raise RuntimeError('Hosted Codex requires a fresh home without auth.json')
    config_file = home / 'config.toml'
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


def event_usage(events):
    completed = [event['usage'] for event in events if event.get('type') == 'turn.completed']
    if len(completed) != 1:
        return None
    usage = completed[0]
    for field in ('input_tokens', 'output_tokens'):
        if type(usage.get(field)) is not int or usage[field] < 0:
            return None
    return {field: usage[field] for field in ('input_tokens', 'cached_input_tokens', 'output_tokens')
            if type(usage.get(field)) is int and usage[field] >= 0}


def invoke():
    batch = load(BATCH, {})
    smoke = batch['task'] == 'smoke-test'
    MODEL.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='venture-edit-') as directory:
        workspace = Path(directory)
        schema, result = workspace / 'schema.json', workspace / 'result.json'
        instructions = workspace / 'instructions.txt'
        instructions.write_text(
            'Call the fixed venture_smoke check tool and return its marker as JSON.' if smoke else
            (REPOSITORY / 'ops/editor.md').read_text()
        )
        try:
            config(smoke, instructions)
        except ValueError:
            save(MODEL / 'usage.json', {'input_tokens': 0, 'output_tokens': 0})
            raise
        prompt = json.dumps(batch, ensure_ascii=False)
        schema_data = output_schema()
        if smoke:
            schema_data = dict(type='object', properties={'marker': {'type': 'string'}},
                               required=['marker'], additionalProperties=False)
            prompt = "Call the venture_smoke check tool once and return its output text as marker."
        save(schema, schema_data)
        command = [
            'codex', 'exec', '--skip-git-repo-check', '--ephemeral', '--json',
            '--sandbox', 'workspace-write' if smoke else 'read-only',
            '--output-schema', str(schema), '-o', str(result), '-',
        ]
        environment = {name: os.environ[name] for name in
                       ('PATH', 'HOME', 'LANG', 'CODEX_API_KEY') if name in os.environ}
        key = environment['CODEX_API_KEY']
        with subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              text=True, cwd=workspace, env=environment, start_new_session=True) as process:
            timed_out = False
            try:
                events_text, errors = process.communicate(prompt, timeout=240)
            except subprocess.TimeoutExpired:
                timed_out = True
                os.killpg(process.pid, signal.SIGKILL)
                events_text, errors = process.communicate()
        redacted_events = events_text.replace(key, '[REDACTED]')
        (MODEL / 'events.jsonl').write_text(redacted_events)
        events = []
        for line in redacted_events.splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                continue
        usage = event_usage(events)
        if usage is not None:
            save(MODEL / 'usage.json', usage)
            print(f'Codex usage {usage}')
        if timed_out or process.returncode or not result.is_file() or usage is None:
            for event in events:
                if event.get('type') in ('error', 'turn.failed'):
                    print(json.dumps(event, ensure_ascii=True))
            if errors:
                print(as_log(errors.replace(key, '[REDACTED]')[-6000:]))
            raise RuntimeError(f'Codex failed (exit={process.returncode}, timeout={timed_out})')
        if usage['input_tokens'] + usage['output_tokens'] > batch['reservation']:
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
        else:
            save(MODEL / 'response.json', response)


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
    if not result.is_file() or result.is_symlink() or result.stat().st_size > 160_000:
        raise ValueError('Missing or invalid model result')
    response = load(result, {})
    if type(response) is not dict or set(response) != {'articles', 'skipped'}:
        raise ValueError('Invalid editorial response')
    if type(response['articles']) is not list or not string_list(response['skipped'], 8, 64):
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
            elif not string_list(value, 8, 64):
                raise ValueError(f'Invalid array {name}')
    before = {(article['collection'], article['slug']) for article in metadata()}
    now = datetime.fromisoformat(batch['now'])
    if now.date().isoformat() != batch['date']:
        raise ValueError('Batch date is invalid')
    skipped = write_articles(response, batch['task'], batch['candidates'], now, batch['maxArticles'])
    articles = metadata()
    items = load(ITEMS, {})
    sync(items, articles)
    for key in skipped:
        if items[key]['status'] in ('pending', 'expired'):
            items[key]['status'] = 'skipped'
    save(ITEMS, items)
    routes = [f"{article['collection']}/{article['slug']}/" for article in articles
              if (article['collection'], article['slug']) not in before]
    save(WORK / 'routes.json', routes)


def string_list(value, count, length):
    return type(value) is list and len(value) <= count and all(
        isinstance(item, str) and 0 < len(item) <= length for item in value
    )


def settle():
    path = WORK / 'result' / 'usage.json'
    if not path.is_file() or path.is_symlink() or path.stat().st_size > 1024:
        return
    usage = load(path, {})
    if type(usage) is not dict or any(type(usage.get(key)) is not int or usage[key] < 0
                                      for key in ('input_tokens', 'output_tokens')):
        raise ValueError('Invalid usage receipt')
    batch = load(BATCH, {})
    ledger_path = STATE / 'usage.json'
    ledger = load(ledger_path, {})
    day = ledger[batch['date']]
    receipt = f"{os.environ['GITHUB_RUN_ID']}-{os.environ['GITHUB_RUN_ATTEMPT']}"
    receipts = day.setdefault('usage', {})
    if receipt not in receipts:
        day['tokens'] += usage['input_tokens'] + usage['output_tokens'] - batch['reservation']
        receipts[receipt] = usage
        save(ledger_path, ledger)


def health(wait=False):
    from urllib.request import Request, urlopen

    base = 'https://codex-venture.com'
    release = Path('dist/release.txt').read_text().strip()
    routes = load(WORK / 'routes.json', [])
    for attempt in range(24 if wait else 1):
        try:
            probe(base, release)
            for route in routes:
                request = Request(f'{base}/{route}?release={release}', headers=PROBE_HEADERS)
                with urlopen(request, timeout=8) as response:
                    page = response.read(2_000_000)
                expected = (Path('dist') / route / 'index.html').read_bytes()
                if page != expected:
                    raise RuntimeError(f'{route} differs from the built article')
            print(f'Public release {release} verified, {len(routes)} new articles')
            return
        except (OSError, RuntimeError) as error:
            if not wait or attempt == 23:
                raise
            print(f'Waiting for Cloudflare deployment: {error}', flush=True)
            time.sleep(20)


if __name__ == '__main__':
    actions = {'prepare': prepare, 'invoke': invoke, 'accept': accept,
               'settle': settle, 'health': health, 'smoke-tool': smoke_tool}
    command, *arguments = sys.argv[1:]
    actions[command](*arguments)
