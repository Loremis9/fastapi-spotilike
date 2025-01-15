from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class AlbumCreate(BaseModel):
    title: str
    pouch: Optional[str]
    artist_id: UUID
    release_date: datetime
    class Config:
        orm_mode = True
    
class AlbumOutput(AlbumCreate):
    album_id: UUID
    class Config:
        orm_mode = True

class AlbumModify(BaseModel):
    album_id: UUID
    title: str
    pouch: Optional[str]
    artist_id: UUID
    release_date: datetime
    class Config:
        orm_mode = True