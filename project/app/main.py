import logging

from fastapi import FastAPI

from app.api.v1.api import api_router
from app.api.v1.endpoints.ping import router
from app.db.init import init_db
from app.core.config import settings

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        description="Videoclub RESTful API",
        version="1.0",
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )
    application.include_router(api_router, prefix="/api/v1")
    application.include_router(router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
