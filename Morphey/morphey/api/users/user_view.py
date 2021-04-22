from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint


class UserView(HTTPEndpoint):
    async def get(self, request):
        return JSONResponse({'ping': 'pong'})

    async def path(self, request):
        pass
