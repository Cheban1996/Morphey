import uvloop
from aiohttp import web
from aiohttp_swagger import setup_swagger

from morphey.routes import client_routes
from morphey.commons.utils import setup_data, setup_redis


async def init_app() -> web.Application:
    app = web.Application()
    client_routes(app)
    await setup_redis(app)
    await setup_data(app)
    setup_swagger(app, ui_version=3)
    return app


if __name__ == '__main__':
    uvloop.install()
    web.run_app(app=init_app(), port=5000)