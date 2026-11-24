"""Record independently completed phases without exposing private fields in the job summary."""
from datetime import datetime
import os
from pathlib import Path
import sys

from analytics import store
from collect import load, save
from editor import DATE_ZONE
from model_cost import configured_price, estimate

WORK = Path(os.getenv('RUNNER_TEMP', '.venture-runtime')) / 'venture'


def record(phase, task):
    start = datetime.fromisoformat(os.environ.get('PHASE_START') or datetime.now(DATE_ZONE).isoformat())
    end = datetime.now(DATE_ZONE)
    status = os.environ.get('PHASE_OUTCOME') or 'unknown'
    routes = load(WORK / 'routes.json', [])
    published = len(routes) if os.getenv('PUSH_OUTCOME') == 'success' else 0
    summary = os.getenv('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a') as handle:
            handle.write(f'| Stage | Status | Seconds |\n| --- | --- | ---: |\n'
                         f'| {phase} | {status} | {(end-start).total_seconds():.0f} |\n')
            if phase == 'publish':
                handle.write(f'\nPublished articles / 已发布文章 **{published}**\n')
    root = store()
    if root is None:
        return
    identity = os.environ['GITHUB_RUN_ID'] + '-' + os.environ['GITHUB_RUN_ATTEMPT']
    # Use the immutable GitHub run date shared by all phases, including across CST midnight.
    day = os.environ['VENTURE_RUN_DAY']
    path = root / 'operations' / day / (identity + '.json')
    run = load(path, {'task': task})
    details = dict(start=start.isoformat(), end=end.isoformat(),
                   seconds=round((end-start).total_seconds(), 3), status=status)
    run[phase] = details
    if phase == 'prepare':
        batch = load(WORK / 'batch.json', {})
        details.update(load(WORK / 'collection.json', {}))
        details['candidates'] = len(batch['candidates']) if batch else None
    elif phase == 'edit':
        receipt = load(WORK / 'model' / 'receipt.json', None)
        response = load(WORK / 'model' / 'response.json', {})
        details['generated'] = len(response.get('articles', []))
        if receipt:
            try:
                price = configured_price(receipt['provider'], receipt.get('model'), day)
                receipt['estimated_cost'] = estimate(receipt['usage'], price)
            except (ValueError, KeyError, ArithmeticError):
                receipt['estimated_cost'] = None
            run['model'] = receipt
    elif phase == 'publish':
        run['published'] = published
        run['reviewed'] = len(routes)
        run['production'] = os.getenv('HEALTH_OUTCOME') or 'unknown'
        run['sha'] = os.getenv('PUBLISH_SHA') or os.environ['GITHUB_SHA']
        run['cloudflare_deployment'] = 'verified_by_release_probe' if (
            run['production'] == 'success' and published) else 'unavailable'
    save(path, run)


if __name__ == '__main__':
    record(*sys.argv[1:])
