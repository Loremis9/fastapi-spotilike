from pydantic import BaseModel
from typing import Optional


class ArtistCreate(BaseModel):
    artist_name: str
    avatar:Optional[str]
    biography: str

class ArtistOutput(BaseModel):
    artist_id: str
    
class ArtistModify(ArtistCreate):
    artist_id: str