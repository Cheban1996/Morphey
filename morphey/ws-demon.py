import asyncio
import json
import os
import logging

import aiohttp
import uvloop
import aioredis
import ccxt.async_support as ccxt


class App:
    redis: aioredis

    async def setup(self):
        host = os.getenv('REDIS_URL', '127.0.0.1')
        port = os.getenv('REDIS_PORT', '6379')
        self.redis = await aioredis.create_redis_pool(f"redis://{host}:{port}")

    async def setup_data(self):
        self.redis.hset('active_symbols', 'btcusdt', '1m')

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.redis.close()
        await self.redis.wait_closed()


class RedisStore:

    @staticmethod
    async def symbols():
        def template(ticker, candle_size):
            return (f"wss://stream.binance.com/stream?"
                    f"streams={ticker.decode()}@kline_{candle_size.decode()}")

        urls = await app.redis.hgetall('active_symbols')
        return [template(ticker, candle_size)
                for ticker, candle_size in urls.items()]


class CCXT(RedisStore):

    def ccxt(self, exchange) -> ccxt.binance:
        return getattr(ccxt, exchange)

    async def get_symbols_exchange(self, exchange='binance'):
        print(await self.ccxt(exchange).load_markets())

    async def get_urls(self):
        return await self.symbols()


class WS:

    @staticmethod
    async def kline(url, session):

        async with session.ws_connect(url) as ws:
            async for msg in ws:

                if msg.data == 'close':
                    await ws.close()
                    break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break
                payload = json.loads(msg.data)['data']
                symbol = payload['s']
                data = json.dumps({"o": payload['k']['o'],
                                   "c": payload['k']['c'],
                                   "h": payload['k']['h'],
                                   "l": payload['k']['l']})
                await app.redis.hset('KLINE', symbol, data)
                print(symbol, data)

    @staticmethod
    async def balance(url):
        pass


async def worker(session, timeout=5):
    urls = await RedisStore.symbols()
    loop = asyncio.get_event_loop()
    global futures
    futures.update({
        url: (asyncio.run_coroutine_threadsafe(WS.kline(url, session), loop))
        for url in urls
        if url not in futures
    })
    while True:
        await asyncio.sleep(timeout)
        new_urls = await RedisStore.symbols()
        if urls != new_urls:
            print('..Reload WS Worker')
            await worker(session)


async def main():
    print('Start WS-DEMON...')
    await app.setup()

    async with aiohttp.ClientSession() as session:
        await worker(session)


if __name__ == '__main__':
    futures = {}
    logger = logging.getLogger('WS-Demon')
    logger.setLevel(logging.DEBUG)
    app = App()
    uvloop.install()
    asyncio.run(main())
