from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from ..artists.service import get_artist_by_id
from uuid import UUID
from ....core.security import return_http_error
from ....core.log.metrics import log_info

def create_album(db: Session, album: schemas.AlbumCreate) -> models.Album:
    db_album = models.Album(**album.dict())
    db_album.title.encode("latin1").decode("utf-8")
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    log_info("create album")
    return db_album

def get_album_by_id(db: Session, album_id: UUID) -> models.Album:
    db_album =  db.query(models.Album).filter(models.Album.album_id == album_id, models.Album.deleted_at.is_(None)).first()
    if not db_album:
        raise return_http_error("Album not found")
    log_info("getAlbum")
    return db_album

def get_album_by_artist_id(db,artist_id, skip : int = 0, limit : int =100):
    db_album = db.query(models.Album).filter(models.Album.artist_id == artist_id, models.Album.deleted_at.is_(None)).offset(skip).limit(limit).all()
    if not db_album:
        raise return_http_error("Album not found for artist")
    log_info("getAlbumByArtistId")
    return db_album

def get_albums(db: Session, skip : int = 0, limit : int =100):
    log_info('getAlbums')
    db_album = db.query(models.Album).filter(models.Album.deleted_at.is_(None)).offset(skip).limit(limit).all()
    if not db_album:
       raise return_http_error("Album not found")
    return db_album

def remove_album(db: Session, album_id: UUID) -> bool:
    album = get_album_by_id(db,album_id)
    if not album:
        raise return_http_error("Album not found")

    db.delete(album)
    db.commit()
    log_info('removeAlbum')
    return True

def put_album(db :Session, album_id: UUID ,album: schemas.AlbumModify) -> models.Album:
    db_album = get_album_by_id(db,album_id)
    if not album:
        raise return_http_error("Album not found")
    if album.release_date:
        db_album.release_date = album.release_date
    if album.title:
        db_album.title = album.title
    if album.artist_id:
        artist = get_artist_by_id(db,album.artist_id)
        if not artist:
            raise return_http_error("Artist not found")
        db_album.artist_id = artist.artist_id
        db_album.artist_name= artist.artist_name.encode("latin1").decode("utf-8")

    db_album.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_album)
    log_info('modifyAlbum')
    return db_album
    
