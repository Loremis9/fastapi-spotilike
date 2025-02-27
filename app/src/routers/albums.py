from fastapi import APIRouter, Depends
from ..models.albums import service as album_service
from ..models.albums.schemas import AlbumOutput, AlbumCreate, AlbumModify
from sqlalchemy.orm import Session
from uuid import UUID
from ...core.database import get_db
from ..models.user_sessions import service as user_session_service
from ..models.users.models import User
from typing import Annotated
from ...core.security import return_http_error
from .converter.album_converter import convert_albums_output, convert_album_output
from ..models.user_sessions.service import oauth2_scheme

router = APIRouter(tags=["albums"])

@router.get("/albums",response_model=list[AlbumOutput])
async def get_all_albums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[AlbumOutput]:
    album = album_service.get_albums(db, skip=skip, limit=limit)
    return convert_albums_output(db, album)


@router.get("/albums/{album_id}",response_model=AlbumOutput)
async def get_albums_id(album_id : UUID, db: Session = Depends(get_db)) -> AlbumOutput:
    album =  album_service.get_album_by_id(db,album_id)
    return convert_album_output(db,album)

@router.get("/albums/artist/{artist_id}",response_model=list[AlbumOutput])
async def get_albums_by_artist_id(artist_id : UUID, db: Session = Depends(get_db)) -> list[AlbumOutput]:
    album = album_service.get_album_by_artist_id(db,artist_id)
    return convert_albums_output(db,album)

@router.post("/albums",response_model=AlbumOutput)
async def get_all_albums(schema:AlbumCreate, db: Session = Depends(get_db)) -> AlbumOutput:
    album= album_service.create_album(db, schema)
    return convert_album_output(db,album)


@router.put("/albums/{album_id}",response_model=AlbumOutput)
async def put_alubms_by_id(album_id : UUID,schema: AlbumModify, db: Session = Depends(get_db)) -> AlbumOutput:
    album= album_service.put_album(db, album_id, schema)
    return convert_album_output(db, album)

@router.delete("/albums/{album_id}",response_model=bool, dependencies=[Depends(oauth2_scheme)])
async def get_song_by_id(album_id : UUID, db: Session = Depends(get_db),user = Annotated[User,Depends(user_session_service.get_current_user)]) -> bool:
    return album_service.remove_album(db,album_id)