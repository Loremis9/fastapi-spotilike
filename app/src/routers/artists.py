from fastapi import APIRouter, Depends
from uuid import UUID
from ...core.database import get_db
from sqlalchemy.orm import Session
from ..models.artists import service as artist_service
from ..models.artists.schemas import ArtistOutput, ArtistModify
from ..models.user_sessions import service as user_session_service
from ..models.users.models import User
from typing import Annotated
from ...core.security import return_http_error


router = APIRouter()

@router.get("/artists",response_model=list[ArtistOutput])
async def get_artists(db: Session = Depends(get_db))-> list[ArtistOutput]:
    db_artist= artist_service.get_artists(db=db)
    if not db_artist:
        raise return_http_error("Album not found")
    return db_artist

@router.put("/artists/{artist_id}",response_model=ArtistOutput)
async def put_artist_by_id(artist_id : UUID, schema : ArtistModify , db: Session = Depends(get_db)) -> ArtistOutput:
    return artist_service.put_artist(artist_id, schema,db)

@router.delete("/artists/{artist_id}",response_model=bool)
async def get_song_by_id(artist_id : UUID, db: Session = Depends(get_db),user = Annotated[User,Depends(user_session_service.get_current_user)]) -> bool:
    return artist_service.remove_album(db,artist_id)