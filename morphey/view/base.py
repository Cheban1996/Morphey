from aiohttp import web
from aiohttp_cors import CorsViewMixin


class Resource(web.View, CorsViewMixin):
    """Resource is Base class for child view"""
    # example swagger
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
