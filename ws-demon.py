import asyncio
import json
import sys
import os

import aiohttp
import uvloop
import aioredis


class App:
    redis: aioredis

    async def setup(self):
        self.redis = await aioredis.create_redis_pool('redis://localhost')

    async def reload(self):
        restart = json.loads(await self.redis.get('restart'))
        if restart is True:
            await self.redis.set('restart', json.dumps(False))
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.redis.close()
        await self.redis.wait_closed()


class Redis(App):
    urls_klines = [
        "wss://stream.binance.com/stream?streams=btcusdt@kline_1m",
        "wss://stream.binance.com/stream?streams=ethbtc@kline_1m",
        "wss://stream.binance.com/stream?streams=bnbbtc@kline_1m",
    ]

    @property
    async def restart(self) -> bool:
        return json.loads(await self.redis.get('restart'))

    @restart.setter
    async def restart(self, restart: bool):
        await self.redis.set('restart', json.dumps(restart))

    @property
    async def symbols(self) -> dict:
        return json.loads(await self.redis.get('symbols'))


class CCXT:
    """CCXT"""


class WS:

    async def kline(self, url):
        async with aiohttp.ClientSession() as session:
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

    async def balance(self, url):
        pass


async def manual_loop(timeout=5):
    await asyncio.sleep(timeout)
    await app.reload()
    await manual_loop()


async def main():
    await app.setup()

    await asyncio.gather(
        *(WS().kline(url) for url in Redis.urls_klines),
        manual_loop()
    )


if __name__ == '__main__':
    app = App()
    uvloop.install()
    asyncio.run(main())
