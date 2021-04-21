import asyncio
import json
import logging
import os

import aiohttp
import uvloop

from model import bifrost_bridge
from store import RedisStore
from app import App
from schemas import StreamKlineSchema

app = App()
redis = RedisStore()


@app.startup()
async def startup():
    await redis.setup()


@app.shutdown()
async def shutdown():
    await redis.close()


async def listen_ws(url, session):
    async with session.ws_connect(url) as ws:
        async for msg in ws:
            if msg.data == 'close':
                await ws.close()
                break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                break

            data = json.loads(msg.data)['data']
            try:
                data = StreamKlineSchema.parse_obj(data)
                print(data.dict())
                await redis.update_price_ticker(data.s, data.json())
                # await bifrost_bridge.create(data.dict())
            except BaseException as e:
                print(e)


async def worker(session, timeout=5):
    urls = await redis.get_symbols()
    loop = asyncio.get_event_loop()
    global futures
    for url in urls:
        if url in futures:
            continue

        future_result = asyncio.run_coroutine_threadsafe(
            listen_ws(url, session),
            loop
        )
        futures[url] = future_result

    while True:
        await asyncio.sleep(timeout)
        new_urls = await redis.get_symbols()
        if urls != new_urls:
            print('..Reload WS Worker')
            await worker(session)


@app.run()
async def main():
    async with aiohttp.ClientSession() as session:
        await worker(session)


if __name__ == '__main__':
    futures = {}
    logger = logging.getLogger('BIFROST-BRIDGE')
    logger.setLevel(logging.DEBUG)
    os.environ["PYTHONASYNCIODEBUG"] = "1"
    uvloop.install()
    asyncio.run(main())
