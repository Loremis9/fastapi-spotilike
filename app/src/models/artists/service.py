from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from uuid import UUID
from ....core.security import return_http_error
from ....core.config import BAD_REQUEST
from ....core.log.metrics import log_info

def create_artist(db: Session, artist: schemas.ArtistCreate) -> models.Artist:
    db_artist = models.Artist(**artist.dict())
    db_existing = db.query(models.Artist).filter(models.Artist.artist_name == db_artist.artist_name).first()
    if db_existing:
        raise return_http_error("Artist already exist", status_http=BAD_REQUEST)
    db_artist.biography.encode("latin1").decode("utf-8")
    db_artist.artist_name.encode("latin1").decode("utf-8")
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    log_info("createArtist")
    return db_artist

def get_artist_by_id(db:Session, artist_id: int) -> models.Artist:
    log_info("getArtistId")
    db_artist= db.query(models.Artist).filter(models.Artist.artist_id == artist_id, models.Artist.deleted_at.is_(None)).first()
    if not db_artist:
        raise return_http_error("Artist not found")
    return db_artist

def get_artists(db:Session, skip : int = 0, limit : int =100) -> list[models.Artist]:
    log_info("getArtists")
    db_artist= db.query(models.Artist).filter(models.Artist.deleted_at.is_(None)).offset(skip).limit(limit).all()
    if not db_artist:
        raise return_http_error("Artist not found")
    return db_artist

def remove_album(db: Session, artist_id: int) -> bool:
    db_artist = get_artist_by_id(db,artist_id)
    if not db_artist:
        raise return_http_error("Artist not found")
    db.delete(db_artist)
    db.commit()
    log_info("removeArtists")
    return True

def put_artist(artist_id : UUID,artist: schemas.ArtistModify,db :Session) -> models.Artist:
    db_artist = get_artist_by_id(db, artist_id)
    if not db_artist:
        raise return_http_error("Artist not found")
    
    if artist.artist_name:
        db_artist.artist_name = artist.artist_name.encode("latin1").decode("utf-8")
    if artist.avatar:
        db_artist.avatar = artist.avatar
    if artist.biography:
        db_artist.biography = artist.biography.encode("latin1").decode("utf-8")

    db_artist.update_at = datetime.utcnow()
    db.commit()
    db.refresh(db_artist)
    log_info("modifyArtist")
    return db_artist

