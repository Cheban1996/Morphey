from aiohttp import web

from morphey.view.base import Resource
from morphey.models.user import User


class UserView(Resource):

    async def get(self):
        """
       ---
       description: This end-point get resource data.
       tags:
       - ResourceData
       produces:
       - text/json
       responses:
           "200":
               description: successful operation. Return "pong" text
           "405":
               description: invalid HTTP Method
        """
        return web.json_response({'data': {'users': await User.get_users()}})

    async def post(self):
        body = await self.request.json()
        response = await User().create_user(**body)
        return web.json_response({'status': response})
