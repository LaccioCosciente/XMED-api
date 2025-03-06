from fastapi import FastAPI
from etc.config import settings

from src.v1.config import routers as config_apis_v1


app = FastAPI(
    debug=True,
    title=settings.TITLE,
    version=settings.VERSION,
    summary=settings.SUMMARY
)

app.include_router(
    config_apis_v1.router,
    prefix="/api/v1/config",
    tags=["config"]
)