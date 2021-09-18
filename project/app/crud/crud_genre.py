from datetime import datetime
from typing import List, Union

from app.models import Genre
from app.schemas import GenreCreate, GenreUpdate


async def get_all() -> List:
    genres = await Genre.all().values()
    return genres


async def post(payload: GenreCreate) -> Genre:
    datetime_now = datetime.now()
    new_genre = await Genre.create(
        **payload.dict(),
        created_at=datetime_now,
        updated_at=datetime_now,
    )
    return new_genre


async def get(id: int) -> Union[dict, None]:
    genre = await Genre.filter(id=id).first().values()
    if genre:
        return genre[0]
    return None


async def put(id: int, payload: GenreUpdate) -> Union[dict, None]:
    # TODO: validate if name is taken
    genre = await Genre.filter(id=id).update(**payload.dict())
    if genre:
        updated_genre = await Genre.filter(id=id).first().values()
        return updated_genre[0]
    return None


async def delete(id: int):
    genre = await Genre.filter(id=id).delete()
    return genre
