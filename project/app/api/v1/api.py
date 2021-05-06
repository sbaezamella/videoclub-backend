from fastapi import APIRouter

from app.api.v1.endpoints import genres

api_router = APIRouter()
api_router.include_router(genres.router, prefix="/genres", tags=["genres"])
