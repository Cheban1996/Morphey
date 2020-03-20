import pytest
import json


async def test_markets(binance):
    json.dumps(await binance().load_markets(), indent=4, sort_keys=True)
