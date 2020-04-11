import asyncio
import json
from datetime import datetime

from aiohttp import (web, WSMsgType)
import marshmallow
from morphey.schemas.user import SchemaUser
from morphey.models.user import User


async def sign_in(request):
    data = SchemaUser().load(await request.json())
    await request.app['redis'].set('symbols', 'XX1')
    return web.json_response(data)


async def sign_up(request):
    try:
        body = await request.json()
        credential: dict = SchemaUser().load(body)
        data = await User().create_user(credential)
        return web.json_response({'data': data})
    except marshmallow.exceptions.ValidationError as e:
        return e.normalized_messages()


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
