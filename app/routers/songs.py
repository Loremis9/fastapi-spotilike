from fastapi import APIRouter, Depends, HTTPException
from ..core.dependencies import get_token_header
from ..models.Artists.service import get_artist_by_id
from ..models.Artists.schemas import ArtistOutput
from ..models.types.schemas import TypeOutput
from ..models.types.service import get_all_types, get_type_by_id
from ..models.Songs.schemas import songOutput
from ..models.Songs.service import get_song_by_album_id, get_song_by_artist_id
from uuid import UUID
from typing import List
from ..core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/api",
    tags=["songs"]
)

@router.get("/artist/{artist_id}/songs",response_model=List[songOutput]) 
async def get_all_song_by_artist_id(artist_id : UUID,db: Session = Depends(get_db)):
    songs =  get_song_by_artist_id(db,artist_id)
    return [songOutput(
            id=song.song_id,
            title=song.title,
            type=song.type_id,
            duration=song.duration,
            album_id=song.album_id,
            artist=song.artist.artist_id
        ) for song in songs]

@router.get("/albums/{albums_id}/songs",response_model=List[songOutput])
async def get_song_by_id(albums_id : UUID,db: Session = Depends(get_db)):
    songs = get_song_by_album_id(db,albums_id)
    return [songOutput(
            id=song.song_id,
            title=song.title,
            type=song.type_id,
            duration=song.duration,
            album_id=song.album_id,
            artist=song.artist.artist_id
        ) for song in songs]

@router.get("/genres", response_model=List[TypeOutput])
async def get_all_genre(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_types(db, skip=skip, limit=limit)

@router.post("/albums/{id}/songs")
async def get_song_by_id(id : int):
    return {"song by id post": id}

@router.put("api/genre/{id}")
async def get_song_by_id(id : int):
    return {"modification genre": id}

@router.delete("/genre/{id}")
async def get_song_by_id(id : int):
    return {"delete genre": id}