import pytest
import json
from morphey.models.exchange import Exchange
import ccxt
from pprint import pprint


async def test_markets(binance):
    json.dumps(await binance().load_markets(), indent=4, sort_keys=True)


async def test_balance():
    e = Exchange(
        1,
        'Xdfiu2NivPj1jOeQUTvq8xfWEO8lVjq4DkBetCQbgHi6ntwuyWm5vxgkQJM3GZXr',
        'K4lFUM7RyVHrYll6V5hTVBKodtydUYg7ElQfL4NpBycfRgSz8OFUuk3BkddMoTRt')
    pprint(await e.exchange.fetch_total_balance())
