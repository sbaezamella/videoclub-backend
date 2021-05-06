from typing import List

from fastapi import APIRouter

from app import models, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Genre])
async def get_genres():
    return await models.Genre.all()
