import logging
import os

from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

from fastapi import FastAPI

log = logging.getLogger(__name__)

config = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.environ.get("POSTGRES_SERVER"),
                "port": os.environ.get("POSTGRES_PORT"),
                "user": os.environ.get("POSTGRES_USER"),
                "password": os.environ.get("POSTGRES_PASSWORD"),
                "database": os.environ.get("POSTGRES_DB"),
            },
        },
    },
    "apps": {
        "models": {
            "models": [
                "app.models.genres",
                "app.models.movies",
            ],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=config,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        config=config,
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(generate_schema())
