import pytest
import json


def test_1():
    assert 1 + 1 == 2


@pytest.mark.asyncio()
async def test_binance(binance):
    print(json.dumps(await binance().load_markets(), indent=4, sort_keys=True))
