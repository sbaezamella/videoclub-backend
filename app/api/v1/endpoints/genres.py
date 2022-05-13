from typing import List

from fastapi import APIRouter, HTTPException, Path, Response, status
from tortoise.exceptions import IntegrityError

from app import models, schemas
from app.crud import crud_genre

router = APIRouter()


@router.get("/", response_model=List[schemas.Genre])
async def get_all_genres() -> List[schemas.Genre]:
    genres = await crud_genre.get_all()
    return genres


@router.post(
    "/", response_model=schemas.Genre, status_code=status.HTTP_201_CREATED
)  # noqa
async def create_genre(payload: schemas.GenreCreate) -> models.Genre:
    try:
        new_genre = await crud_genre.post(payload)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Genre already exists",
        )
    return new_genre


@router.get("/{id}", response_model=schemas.Genre)
async def get_genre(id: int = Path(..., ge=1)):
    genre = await crud_genre.get(id)
    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Genre not found",
        )
    return genre


@router.put("/{id}", response_model=schemas.Genre)
async def update_genre(payload: schemas.GenreUpdate, id: int = Path(..., ge=1)):
    # TODO: validate if name is taken
    genre = await crud_genre.put(id, payload)

    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Genre not found",
        )

    return genre


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_genre(id: int = Path(..., ge=1)):
    genre = await crud_genre.delete(id)
    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Genre not found",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
