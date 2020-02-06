import asyncio
import pytest
import ccxt.async_support as ccxt


@pytest.fixture
def binance() -> ccxt.binance:
    yield ccxt.binance
