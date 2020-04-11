from morphey.models.exchange import Exchange
from morphey.services.exchange import ServiceExchange
import aioredis
from aioredis import Redis
import json


async def setup_data(app):
    """
    This function set data for correct work Morphey application
    1. set in redis market
    2.  set in redis symbols
    """

    redis: Redis = app['redis']
    exchange = ServiceExchange()
    markets, symbols = await exchange.fetch_markets()
    await redis.set('market', json.dumps(markets))
    await redis.set('symbols', json.dumps(symbols))


async def setup_redis(app) -> Redis:
    redis = None
    try:
        redis = await aioredis.create_redis_pool(
            f"redis://localhost:6379"
        )
    except ConnectionError:
        print("!!! Can't connect to Redis server !!!")
        exit(1)

    async def close_redis(app):
        redis.close()
        await redis.wait_closed()

    app.on_cleanup.append(close_redis)
    app['redis'] = redis
    return redis
