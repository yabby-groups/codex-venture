"""Codex session receipts and effective-dated provider price estimates."""
from decimal import Decimal
import os

from collect import load
from pathlib import Path


def event_usage(events):
    completed = [event.get('usage') for event in events if event.get('type') == 'turn.completed']
    if len(completed) != 1 or not isinstance(completed[0], dict):
        return None
    usage = completed[0]
    fields = ('input_tokens', 'output_tokens', 'cached_input_tokens', 'reasoning_output_tokens')
    observed = {key: usage[key] for key in fields
                if type(usage.get(key)) is int and usage[key] >= 0}
    return observed if all(key in observed for key in fields[:2]) else None


def price_for(prices, provider, model, day):
    return max((row for row in prices if row['provider'] == provider and row['model'] == model
                and row['effective'] <= day), default=None, key=lambda row: row['effective'])


def estimate(usage, price):
    if usage is None or price is None:
        return None
    input_tokens, output_tokens = usage['input_tokens'], usage['output_tokens']
    cached, reasoning = usage.get('cached_input_tokens'), usage.get('reasoning_output_tokens')
    input_rate = Decimal(str(price['input_per_million']))
    cache_rate = Decimal(str(price['cached_input_per_million']))
    output_rate = Decimal(str(price['output_per_million']))
    if min(input_rate, cache_rate, output_rate) < 0:
        raise ValueError('Negative token rate')
    if cached is None and (input_rate != cache_rate or not price['cache_in_input']):
        return None
    if reasoning is None and not price['reasoning_in_output']:
        return None
    cached, reasoning = cached or 0, reasoning or 0
    if price['cache_in_input']:
        input_tokens -= cached
    if price['reasoning_in_output'] and reasoning > output_tokens or input_tokens < 0:
        return None
    output_tokens += 0 if price['reasoning_in_output'] else reasoning
    amount = (input_tokens * input_rate + cached * cache_rate + output_tokens * output_rate) / 1_000_000
    return {'amount': str(amount), 'currency': price['currency']}


def configured_price(provider, model, day):
    # Overrides are private when provider rates are confidential.
    import json
    prices = json.loads(os.getenv('VENTURE_MODEL_PRICING_JSON') or 'null')
    if prices is None:
        prices = load(Path('config/model-pricing.json'), [])
    return price_for(prices, provider, model, day)


def worst_case(price, tokens):
    if price is None:
        return None
    rate = max(Decimal(str(price[key])) for key in
               ('input_per_million', 'cached_input_per_million', 'output_per_million'))
    return rate * tokens / 1_000_000
