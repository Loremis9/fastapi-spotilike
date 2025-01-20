from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class songCreate(BaseModel):
    title:str
    duration: int
    type: Optional[str]

    
class songOutput(BaseModel):
    title:str
    duration: int
    type: Optional[UUID]
    album_id: UUID
    artist_id: UUID
    song_id: UUID

class ArtistSongOutput(BaseModel):
    artist_name: str
    artist_id: UUID

class AlbumSongOutput(BaseModel):
    title: str
    album_id: UUID