from datetime import datetime

from aiohttp import (web, WSMsgType)
from aiohttp_swagger import setup_swagger
import functools
import uvloop


def auth_client(hendled):
    """Auth Client"""

    @functools.wraps(hendled)
    def wrapper():
        return hendled()

    return wrapper


def auth_admin():
    """Auth Admin"""


class View(web.View):
    async def get(self):
        """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Health check
    produces:
    - text/plain
    responses:
        "200":
            description: successful operation. Return "pong" text
        "405":
            description: invalid HTTP Method
    """
        return web.json_response({'ping': 'pong'})

    async def post(self):
        """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Create User
    produces:
    - text/plain
    responses:
        "200":
            description: successful operation. Return "pong" text
        "405":
            description: invalid HTTP Method
    """
        pass

    async def path(self):
        pass

    async def delete(self):
        pass


def client_routes(app):
    app.router.add_view('/', View)
    app.router.add_get('/ws', websocket_handler)


def admin_routes(app):
    pass


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_json({'time': str(datetime.now())})
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())

    print('websocket connection closed')

    return ws


uvloop.install()
app = web.Application()
client_routes(app)
setup_swagger(app, swagger_url="/api/v1/doc", ui_version=2)
web.run_app(app)
