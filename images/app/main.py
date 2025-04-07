import logging
from fastapi import FastAPI
from etc.config import settings
from src.v1.test import routers as config_apis_v1
from src.v1.agent import routers as agent_apis_v1
from fastapi.middleware.cors import CORSMiddleware
from libs.logger.middleware import JsonLoggingMiddleware
from libs.aiohttp.middleware import AIOHTTPConnectionMiddleware


app = FastAPI(
    debug=True,
    title=settings.TITLE,
    version=settings.VERSION,
    summary=settings.SUMMARY
)

# =====================================

# Json Logger middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(JsonLoggingMiddleware)
app.add_middleware(AIOHTTPConnectionMiddleware)

# =============== Routes ==================

app.include_router(
    config_apis_v1.router,
    prefix="/api/v1/test",
    tags=["test"]
)

app.include_router(
    agent_apis_v1.router,
    prefix="/api/v1/agent",
    tags=["agent"]
)


#  =============== Turn off logs ===============
# Comment to enable logs
logging.getLogger("fastapi").setLevel(logging.CRITICAL)
logging.getLogger("uvicorn").setLevel(logging.CRITICAL)
logging.getLogger("uvicorn.error").setLevel(logging.CRITICAL)
logging.getLogger("uvicorn.access").setLevel(logging.CRITICAL)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, log_level="debug")
