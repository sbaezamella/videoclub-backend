import logging
import os

from pydantic import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    api_v1_str: str = "/api/v1"
    # SECRET_KEY: str
    # PG_DSN: PostgresDsn = "postgres://postgres:password@localhost/videoclub"

    project_name: str = "Videoclub API"

    postgres_host: str = os.environ.get("POSTGRES_HOST", "localhost")
    postgres_port: int = os.environ.get("POSTGRES_PORT", 5432)
    postgres_user: str = os.environ.get("POSTGRES_USER", "postgres")
    postgres_password: str = os.environ.get("POSTGRES_PASSWORD", "password")
    postgres_database: str = os.environ.get("POSTGRES_DATABASE", "videoclub")
    environment: str = os.environ.get("ENVIRONMENT", "development")
    testing: bool = os.environ.get("TESTING", 0)


log.info("Loading config settings from the environment...")
settings = Settings()
