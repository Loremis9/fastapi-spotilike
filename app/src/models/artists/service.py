from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from datetime import datetime
from uuid import UUID
from ....core.security import return_http_error
def create_artist(db: Session, artist: schemas.ArtistCreate) -> models.Artist:
    db_artist = models.Artist(**artist.dict())
    db_artist = encode_str_artist(db_artist)
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_artist_by_id(db:Session, artist_id: int) -> models.Artist:
    return db.query(models.Artist).filter(models.Artist.artist_id == artist_id, models.Artist.deleted_at.is_(None)).first()

def remove_album(db: Session, artist_id: int) -> bool:
    db_artist = get_artist_by_id(db,artist_id)
    if not db_artist:
        raise return_http_error("Artist not found")
    db.delete(db_artist)
    db.commit()
    return True

def put_artist(artist_id : UUID,artist: schemas.ArtistModify,db :Session) -> models.Artist:
    db_artist = get_artist_by_id(db, artist_id)
    if not db_artist:
        raise return_http_error("Artist not found")
    
    if artist.artist_name:
        db_artist.artist_name = artist.artist_name
    if artist.artist_pouch:
        db_artist.pouch = artist.pouch
    if artist.avatar:
        db_artist.avatar = artist.avatar
    if artist.biography:
        db_artist.biography = artist.biography

    db_artist.update_at = datetime.utcnow()
    db_artist = encode_str_artist(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def encode_str_artist(artist: models.Artist) -> models.Artist:
    artist.artist_name = artist.artist_name.encode('utf-8')
    artist.biography = artist.biography.encode('utf-8')
    return artist