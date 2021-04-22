from starlette.routing import Route

from morphey.api.users.user_view import UserView

routes = [
    Route("/user", UserView)
]
