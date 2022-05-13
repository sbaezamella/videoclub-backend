from app.api.v1.endpoints import genres, movies
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(genres.router, prefix="/genres", tags=["genres"])
api_router.include_router(movies.router, prefix="/movies", tags=["movies"])
