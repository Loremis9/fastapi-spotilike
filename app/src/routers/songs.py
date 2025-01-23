from fastapi import APIRouter, Depends, HTTPException
from ..models.types.schemas import TypeOutput, TypeModify
from ..models.types import service as service_type
from ..models.songs.schemas import songOutput, songCreate
from ..models.songs import service as service_song
from uuid import UUID
from typing import List
from ...core.database import get_db
from sqlalchemy.orm import Session
from .converter.song_converter import convert_song_output,convert_songs_output
from ..models.user_sessions import service as service_user_session
from ..models.users.models import User
from typing import Annotated


router = APIRouter()


@router.get("/artist/{artist_id}/songs",response_model=List[songOutput]) 
async def get_all_song_by_artist_id(artist_id : UUID,db: Session = Depends(get_db)) -> songOutput:
    songs =  service_song.get_song_by_artist_id(db,artist_id)
    return convert_songs_output(songs)

@router.get("/albums/{albums_id}/songs",response_model=List[songOutput])
async def get_song_by_id(albums_id : UUID,db: Session = Depends(get_db)) -> songOutput:
    songs = service_song.get_song_by_album_id(db,albums_id)
    return convert_songs_output(songs)

@router.get("/genres", response_model=List[TypeOutput])
async def get_all_genre(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) ->TypeOutput :
    return service_type.get_all_types(db, skip=skip, limit=limit)

@router.post("/albums/{albums_id}/songs",response_model=songOutput)
async def create_song_by_id(albums_id : UUID, songs: songCreate , db: Session = Depends(get_db)) -> songOutput:
    song = service_song.add_song_to_album(db, albums_id,songs)
    return convert_song_output(song)

@router.put("api/genre/{genre_id}",response_model=TypeOutput)
async def modify_types_by_id(genre_id : UUID,schema: TypeModify, db: Session = Depends(get_db)) ->TypeOutput :
    return service_type.put_type(db, genre_id, schema)

@router.delete("/genre/{genre_id}", response_model=bool)
async def delete_song_by_id(genre_id : UUID, db: Session = Depends(get_db), user = Annotated[User,Depends(service_user_session.get_current_user)]) -> bool:
    return service_type.remove_type(db,genre_id)