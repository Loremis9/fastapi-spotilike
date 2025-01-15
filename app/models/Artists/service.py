from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from datetime import datetime


def create_artist(db: Session, album: schemas.ArtistCreate):
    db_artist = models.Artist(**album.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_artist_by_id(db:Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.artist_id == artist_id.artist_id, models.Artist.deleted_at == False).first()

def remove_album(db: Session, artist_id: int):
    db_artist = get_artist_by_id(artist_id)
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    db.delete(db_artist)
    db.commit()
    return True

def put_artist(db :Session, artist: schemas.ArtistModify):
    db_artist = get_artist_by_id(artist.artist_id)
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    db_artist.pouch = artist.artist_name
    db_artist.release_date = artist.avatar
    db_artist.title = artist.biography
    db_artist.update_at = datetime.now(datetime.timezone.utc)
    db.commit()
    return db_artist
    
