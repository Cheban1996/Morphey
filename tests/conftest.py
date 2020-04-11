import pytest
import ccxt.async_support as ccxt
from morphey.app import init_app


@pytest.fixture
def binance() -> ccxt.binance:
    yield ccxt.binance


@pytest.fixture(autouse=True)
async def client(aiohttp_client):
    app = await init_app()
    yield await aiohttp_client(app)


@pytest.fixture
async def redis():
    import aioredis
    redis = await aioredis.create_redis_pool(
        f"redis://localhost:6379"
    )
    yield redis
    await redis.flushall()
    redis.close()
    await redis.wait_closed()


async def db():
    pass


async def user():
    pass
