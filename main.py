from typing import List

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import models
import schemas

app = FastAPI()

register_tortoise(
    app,
    db_url="postgres://postgres:password@db/videoclub",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
async def ping():
    return {"ping": "pong"}


@app.get("/genres", response_model=List[schemas.Genre])
async def get_genres():
    return await models.Genre.all()
