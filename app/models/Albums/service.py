from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from datetime import datetime
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

def put_album(db :Session, album: schemas.AlbumModify):
    db_album = get_album_by_id(album.album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    
    #db_album.artist_id = album.artist_id
    db_album.pouch = album.pouch
    db_album.release_date = album.release_date
    db_album.title = album.title
    db_album.artist_id = album.artist_id
    db_album.updated_at = datetime.now(datetime.timezone.utc)
    db.commit()
    return db_album
    
