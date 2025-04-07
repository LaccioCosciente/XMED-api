from fastapi import FastAPI
from etc.config import settings
from src.v1.test import routers as config_apis_v1
from src.v1.calc import routers as agent_apis_v1
from fastapi.middleware.cors import CORSMiddleware
from libs.logger.middleware import JsonLoggingMiddleware


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

# =============== Routes ==================

app.include_router(
    config_apis_v1.router,
    prefix="/api/v1/test",
    tags=["test"]
)

app.include_router(
    agent_apis_v1.router,
    prefix="/api/v1/calc",
    tags=["calc"]
)
