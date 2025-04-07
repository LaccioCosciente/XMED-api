import aiohttp
from typing import Callable
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

# client = aiohttp.ClientSession()


class AIOHTTPConnectionMiddleware(BaseHTTPMiddleware):
    """
    aiohttp session Middleware
    """

    def __init__(
            self,
            app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(
            self,
            request: Request,
            call_next: Callable) -> Response:

        # do something before router call
        # add db request.state

        request.state.session = aiohttp.ClientSession()

        # process the request and get the response
        response = await call_next(request)

        await request.state.session.close()

        # do something after
        return response
