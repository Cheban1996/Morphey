import aiohttp_cors
from morphey.view.view import (
    websocket_handler,
    sign_in,
    sign_up
)

from morphey.view.user import (
    UserView
)

from morphey.view.exchange import (
    Symbols
)


def client_routes(app):
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(allow_credentials=True,
                                          expose_headers="*",
                                          allow_headers="*")
    })
    cors.add(app.router.add_post('/api/sign_in', sign_in))
    cors.add(app.router.add_post('/api/sign_up', sign_up))
    cors.add(app.router.add_view('/api/user', UserView))
    cors.add(app.router.add_view('/api/symbols', Symbols))

    cors.add(app.router.add_get('/ws', websocket_handler))
