from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ArtistCreate(BaseModel):
    artist_name: str
    avatar:Optional[str]
    biography: str

class ArtistOutput(ArtistCreate):
    artist_id: UUID
    
class ArtistModify(BaseModel):
    artist_name: Optional[str]
    avatar: Optional[str]
    biography: Optional[str]
