import functools

import uvloop
from aiohttp_swagger import setup_swagger
from aiohttp import web

from morphey.routes import client_routes
from morphey.commons.utils import initialize_application, setup_redis


async def application() -> web.Application:
    app = web.Application()
    client_routes(app)
    await setup_redis(app)
    await initialize_application(app)
    setup_swagger(app, ui_version=3)
    return app


if __name__ == '__main__':
    uvloop.install()
    web.run_app(app=application(), port=5000)