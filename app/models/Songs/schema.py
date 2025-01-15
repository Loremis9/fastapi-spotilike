from pydantic import BaseModel
from typing import List

class songCreate(BaseModel):
    title:str
    duration: int
    album_id: str
    artist: List[str]
    
class sonngOutput(songCreate):
    id: str