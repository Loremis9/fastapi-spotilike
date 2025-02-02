from sqlalchemy.orm import Session
from fastapi import HTTPException
from .schemas import songCreate
from ..albums.models import Album 
from .models import Song
from uuid import UUID
from ..artists.models import Artist
from ..albums.service import get_album_by_id
from ..types.service import get_type_by_name
from ....core.security import return_http_error
from ....core.log.metrics import log_info_console

def get_song_by_album_id(db: Session, album_id: UUID) -> Song:
    album = db.query(Album).filter(Album.album_id == album_id, Album.deleted_at.is_(None)).first()
    if album:
        return album.album_song_relationship
    else:
        return None

def get_song_by_artist_id(db: Session, artist_id: UUID) -> Song:
    artist = db.query(Artist).filter(Artist.artist_id == artist_id, Artist.deleted_at.is_(None)).first()
    if artist:
        return artist.songs
    else:
        return None
    
def add_song_to_album(db_session : Session, album_id: str, schema: songCreate) ->  Song:
    album = get_album_by_id(db_session, album_id) 
    type = get_type_by_name(db_session, schema.type)
    if not album:
        raise return_http_error("Album not found")
    if not type:    
        raise return_http_error("Type not found")
    if album:
        new_song = convert_model(schema, album)
        album.album_song_relationship.append(new_song)
        db_session.add(new_song)
        db_session.commit()
        log_info_console("create song")
        return new_song
    else:
        return None 
    
def convert_model(schema : songCreate, album : Album) -> Song:
     new_song = Song(
            title=schema.title.encode('utf-8'),
            artist_id=album.artist_id,
            duration=schema.duration,
            type_id=type.type_id,
            album_id=album.album_id,
            updated_at=None,  
            deleted_at=None,
        )