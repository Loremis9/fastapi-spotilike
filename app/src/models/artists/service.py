from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from datetime import datetime
from uuid import UUID

def create_artist(db: Session, artist: schemas.ArtistCreate):
    db_artist = models.Artist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_artist_by_id(db:Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.artist_id == artist_id, models.Artist.deleted_at.is_(None)).first()

def remove_album(db: Session, artist_id: int):
    db_artist = get_artist_by_id(artist_id)
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    db.delete(db_artist)
    db.commit()
    return True

def put_artist(artist_id : UUID,artist: schemas.ArtistModify,db :Session):
    db_artist = get_artist_by_id(db, artist_id)
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    if artist.artist_name:
        db_artist.pouch = artist.pouch
    if artist.avatar:
        db_artist.avatar = artist.avatar
    if artist.biography:
        db_artist.biography = artist.biography

    db_artist.update_at = datetime.utcnow()
    db.commit()
    db.refresh(db_artist)
    return db_artist
    