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
        from_attributes = True
    
class AlbumOutput(AlbumCreate):
    album_id: UUID
    class Config:
        from_attributes = True

class AlbumModify(BaseModel):
    title: Optional[str]
    pouch: Optional[str]
    artist_id:Optional[UUID]
    release_date: Optional[datetime]
    class Config:
        from_attributes = True