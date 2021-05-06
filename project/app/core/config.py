import logging
import os

from pydantic import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # SECRET_KEY: str
    # PG_DSN: PostgresDsn = "postgres://postgres:password@localhost/videoclub"

    PROJECT_NAME: str

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "development")
    TESTING: bool = os.environ.get("TESTING", 0)

    class Config:
        case_sensitive = True


log.info("Loading config settings from the environment...")
settings = Settings()
