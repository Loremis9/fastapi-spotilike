from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ArtistCreate(BaseModel):
    artist_name: str
    avatar:Optional[str]
    biography: str

class ArtistOutput(ArtistCreate):
    artist_id: UUID
    
class ArtistModify(ArtistCreate):
    artist_name: Optional[str]
    avatar: Optional[str]
    biography: Optional[str]

class ArtistDelete(BaseModel):
    is_deleted: bool