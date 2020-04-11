import os
import asyncio
import aioredis
from aiohttp import ClientSession

host = os.getenv('REDIS_URL', '127.0.0.1')
port = os.getenv('REDIS_PORT', '6379')


async def start_bot(ctx, symbol):
    while True:
        data = await ctx['redis'].hget('KLINE', symbol.upper())
        # if not data:
        #     print(f'Not Found symbol: {symbol}')
        #     raise BaseException(f'Not Found symbol: {symbol}')
        balance = 0.032
        print(symbol, data)
        await asyncio.sleep(0.5)


async def startup(ctx):
    ctx['session'] = ClientSession()
    ctx['redis'] = await aioredis.create_redis_pool(f"redis://{host}:{port}")


async def shutdown(ctx):
    await ctx['session'].close()

    ctx['redis'].close()
    await ctx['redis'].wait_closed()


class WorkerSettings:
    functions = [start_bot]
    on_startup = startup
    on_shutdown = shutdown
    job_timeout = 10**10
