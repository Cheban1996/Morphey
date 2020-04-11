import asyncio
from arq import create_pool
from arq.connections import RedisSettings


async def main():
    redis = await create_pool(RedisSettings())
    for symbol in ['btcusdt', 'bnbusdt', 'ethusdt']:
        await redis.enqueue_job('start_bot', symbol)


asyncio.run(main())