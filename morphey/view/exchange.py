import json
from aiohttp import web

from morphey.view.base import Resource


class Exchange(Resource):
    async def get(self):
        pass

    async def post(self):
        pass

    async def delete(self):
        pass


class Symbols(Resource):
    async def get(self):
        symbols = await self.request.app['redis'].get('symbols')
        return web.json_response(
            {'data': json.loads(symbols)}
        )
