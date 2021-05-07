import logging

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

# import os


log = logging.getLogger(__name__)


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url="postgres://postgres:password@db/videoclub",
        modules={"models": ["app.models.genres"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url="postgres://postgres:password@db/videoclub",
        modules={"models": ["app.models.genres"]},
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(generate_schema())
