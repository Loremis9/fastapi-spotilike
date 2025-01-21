from fastapi import APIRouter, Depends
from ..models.songs.schemas import songOutput
from ..models.songs import service as service_song
from uuid import UUID
from typing import List
from ...core.database import get_db
from sqlalchemy.orm import Session
from .converter.song_converter import convert_songs_output
from ..models.artists import service as service_artist
from ..models.artists.schemas import ArtistOutput, ArtistModify
from ..models.user_session import service as service_user_session

router = APIRouter()

@router.get("/artist/{artist_id}/songs",response_model=List[songOutput]) 
async def get_all_song_by_artist_id(artist_id : UUID,db: Session = Depends(get_db)):
    songs =  service_song.get_song_by_artist_id(db,artist_id)
    return convert_songs_output(songs)

@router.put("/artist/{artist_id}",response_model=ArtistOutput)
async def put_artist_by_id(artist_id : UUID, schema : ArtistModify , db: Session = Depends(get_db)):
    return service_artist.put_artist(artist_id, schema,db)

@router.delete("/artist/{artist_id}")
async def get_song_by_id(artist_id : UUID, db: Session = Depends(get_db),user = Depends(service_user_session.get_current_user)):
    return service_artist.remove_album(artist_id)