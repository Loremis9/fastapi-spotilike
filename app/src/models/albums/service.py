from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from datetime import datetime
from ..artists.service import get_artist_by_id
from uuid import UUID
def create_album(db: Session, album: schemas.AlbumCreate):
    db_album = models.Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

def get_album_by_id(db: Session, album_id: int):
    return db.query(models.Album).filter(models.Album.album_id == album_id, models.Album.deleted_at.is_(None)).first()

def get_albums(db: Session, skip : int = 0, limit : int =100):
    return db.query(models.Album).filter(models.Album.deleted_at.is_(None)).offset(skip).limit(limit).all()

def remove_album(db: Session, album_id: int):
    album = get_album_by_id(album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    db.delete(album)
    db.commit()
    return True

def put_album(db :Session, album_id: UUID ,album: schemas.AlbumModify):
    db_album = get_album_by_id(db,album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    if album.pouch:
        db_album.pouch = album.pouch
    if album.release_date:
        db_album.release_date = album.release_date
    if album.title:
        db_album.title = album.title
    if album.artist_id:
        artist = get_artist_by_id(db,album.artist_id)
        if not artist:
            raise HTTPException(status_code=404, detail="Artist not found")
        db_album.artist_id = artist.artist_id

    db_album.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_album)
    return db_album
    
