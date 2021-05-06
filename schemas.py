from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class GenreBase(BaseModel):
    name: Optional[str]
    created_at: datetime
    updated_at: datetime


# Properties to receive on genre creation
class GenreCreate(GenreBase):
    name: str


# Properties to receive on genre update
class GenreUpdate(GenreBase):
    pass


# Properties shared by models stored in DB
class GenreInDBBase(GenreBase):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime


# Properties to return to client
class Genre(GenreInDBBase):
    pass


# Properties stores in DB
class GenreInDB(GenreInDBBase):
    pass
