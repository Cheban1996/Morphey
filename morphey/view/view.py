import asyncio
import json
from datetime import datetime

from aiohttp import (web, WSMsgType)

from morphey.schemas.user import SchemaUser


async def sign_in(request):
    data = SchemaUser().load(await request.json())
    # print(data)
    # print(request.app.__dict__)
    print(await request.app['redis'].get('symbols'))
    return web.json_response({'data': 'ok'})


async def sign_up(request):
    return web.json_response({'data': 'ok'})


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                while True:
                    data = await request.app['redis'].hgetall('KLINE')
                    data = {key.decode(): json.loads(value) for key, value in data.items()}
                    await ws.send_json(data)
                    await asyncio.sleep(1)
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())

    return ws
