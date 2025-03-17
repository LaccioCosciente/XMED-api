import time
from typing import Callable
from .config import get_logger
from secrets import token_hex
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = get_logger()


class JsonLoggingMiddleware(BaseHTTPMiddleware):

    """
    LoggingMiddleware
    """

    def __init__(
            self,
            app: FastAPI
        ) -> None:
        super().__init__(app)

    async def dispatch(
            self,
            request: Request,
            call_next: Callable
        ) -> Response:

        # do something before router call
        self.stopwatch_start = time.time()

        # add logger to request.state
        request.state.log = logger
        request.state.extra_log = {
            "request_id": token_hex(8),
            "url": request.url,
            "method": request.method,
            "request_path": request.url.path
        }

        request.state.log.info(
            'Request started',
            extra=request.state.extra_log
        )

        # process the request and get the response
        response = await call_next(request)

        request.state.extra_log["response_code"] = response.status_code
        request.state.extra_log["request_time"] = time.time() - self.stopwatch_start
        # do something after
        # log request execution time
        request.state.log.info(
            'Request completed',
            extra=request.state.extra_log
        )
        return response
