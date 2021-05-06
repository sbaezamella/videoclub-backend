from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.v1.api import api_router

app = FastAPI()

register_tortoise(
    app,
    db_url="postgres://postgres:password@db/videoclub",
    modules={"models": ["app.models.genres"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/ping")
async def ping():
    return {"ping": "pong"}


app.include_router(api_router, prefix="/api/v1")
