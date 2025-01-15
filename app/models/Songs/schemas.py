from pydantic import BaseModel
from uuid import UUID
from ...models.Artists.schemas import ArtistOutput
from typing import Optional
class songCreate(BaseModel):
    title:str
    duration: int
    type: Optional[UUID]
    album_id: UUID
    artist: UUID
    
    class Config:
        orm_mode = True
    
class songOutput(songCreate):
    id: UUID

    class Config:
        from_attributes = True