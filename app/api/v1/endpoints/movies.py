import asyncio
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from tortoise.exceptions import IntegrityError

from app import models, schemas
from fastapi import APIRouter, HTTPException, status

router = APIRouter()


# Shared properties
class MovieBase(BaseModel):
    title: Optional[str]
    year: Optional[int]
    stock: Optional[int]
    duration: Optional[int]
    genres: Optional[List[schemas.GenreCreate]]


# Properties to receive on movie creation
class MovieCreate(MovieBase):
    title: str
    year: int
    stock: int
    duration: int
    genres: List[schemas.GenreCreate]


# Properties to receive on movie update
class MovieUpdate(MovieBase):
    pass


# Properties shared by models stored in DB
class MovieInDBBase(MovieBase):
    id: int
    title: str
    year: int
    stock: int
    duration: int
    created_at: datetime
    updated_at: datetime


# Properties to return to client
class Movie(MovieInDBBase):
    pass


@router.get("/", response_model=List[Movie])
async def get_all_movies() -> List[Movie]:
    movies = await models.Movie.all().values()
    return movies


@router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)  # noqa
async def create_movie(payload: MovieCreate) -> Movie:
    datetime_now = datetime.now()
    genres = [await models.Genre.get(**genre) for genre in payload.dict()["genres"]]
    await asyncio.wait(genres)

    new_payload = {
        "title": payload.title,
        "year": payload.year,
        "stock": payload.stock,
        "duration": payload.duration,
    }

    try:
        new_movie = await models.Movie.create(
            **new_payload,
            created_at=datetime_now,
            updated_at=datetime_now,
        )
        await new_movie.genres.add(*genres)
        print(new_movie)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Movie already exists",
        )
    return new_movie


# @router.get("/{id}", response_model=schemas.Genre)
# async def get_genre(id: int = Path(..., ge=1)):
#     genre = await crud_genre.get(id)
#     if not genre:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Genre not found",
#         )
#     return genre


# @router.put("/{id}", response_model=schemas.Genre)
# async def update_genre(payload: schemas.GenreUpdate, id: int = Path(..., ge=1)):
#     # TODO: validate if name is taken
#     genre = await crud_genre.put(id, payload)

#     if not genre:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Genre not found",
#         )

#     return genre


# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_genre(id: int = Path(..., ge=1)):
#     genre = await crud_genre.delete(id)
#     if not genre:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Genre not found",
#         )
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
