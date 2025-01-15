from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas
from ..Albums.models import Album as Album_Model
from .models import Song
from datetime import datetime
from uuid import UUID
from ..Artists.models import Artist


def get_song_by_album_id(db: Session, album_id: UUID):
    album = db.query(Album_Model).filter(Album_Model.album_id == album_id, Album_Model.deleted_at.is_(None)).first()
    if album:
        return album.album_song_relationship
    else:
        return None

def get_song_by_artist_id(db: Session, artist_id: UUID):
    artist = db.query(Artist).filter(Artist.artist_id == artist_id, Artist.deleted_at.is_(None)).first()
    if artist:
        return artist.artist_song_relationship
    else:
        return None
    
def add_song_to_album(db_session, album_id, song_title, song_duration):
    album = db_session.query(Album_Model).filter(Album_Model.album_id == album_id, Album_Model.deleted_at.is_(None)).first()
    if album:
        new_song = Song(
            title=song_title,
            duration=song_duration,
            updated_at=datetime.now(datetime.timezone.utc),  
            deleted_at=None,
        )
        
        # Ajout du Tracking à l'album via la relation
        album.album_tracking_relationship.append(new_song)
        
        # Commit pour enregistrer les changements dans la base de données
        db_session.add(new_song)
        db_session.commit()
        return new_song  # Renvoie le nouveau Tracking ajouté
    else:
        return None 