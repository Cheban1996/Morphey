import asyncio
import pytest

from aiohttp import web
import ccxt.async_support as ccxt
from morphey.app import application
from morphey.commons.utils import initialize_application, setup_redis
from morphey.routes import client_routes


@pytest.fixture
def binance() -> ccxt.binance:
    yield ccxt.binance


# @pytest.fixture(scope='session')
# def loop():
#     loop = asyncio.get_event_loop()
#     yield loop
#     loop.close()


@pytest.fixture
def app():
    app = web.Application()
    client_routes(app)
    yield app


@pytest.fixture
def client(loop, aiohttp_client, app):
    yield loop.run_until_complete(aiohttp_client(app))
    # aiohttp_client.clear()
    # l = asyncio.get_event_loop()
    # l.close()
    #
    # print(loop.__dict__)
    #
    # try:
    #     yield loop.run_until_complete(aiohttp_client(app))
    #     loop.close()
    # finally:
    #     try:
    #         # _cancel_all_tasks(loop)
    #         loop.run_until_complete(loop.shutdown_asyncgens())
    #     finally:
    #         # events.set_event_loop(None)
    #         loop.close()


@pytest.fixture
async def redis(app):
    _redis = await setup_redis(app)
    print(await _redis.get('symbols'))
    yield _redis
    await _redis.flushall()
    print('S')
    _redis.close()
    await _redis.wait_closed()


@pytest.fixture
async def init_app(app):
    await initialize_application(app)
