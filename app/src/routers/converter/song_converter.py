from ...models.songs.models import Song
from ...models.songs.schemas import songOutput,songCreate
from datetime import datetime
from ...models.albums.models import Album as Album_Model
from ...models.artists.models import Artist
from ...models.albums.service import get_album_by_id
from ...models.artists.service import get_artist_by_id
from sqlalchemy.orm import Session

def convert_songs_output(db: Session,songs : Song) -> list[songOutput]:
    list = []
    
    for song in songs:
        album = get_album_by_id(db, song.album_id)
        artist = get_artist_by_id(db,song.artist.artist_id)
        list.append(songOutput(
            song_id=song.song_id,
            title=song.title,
            type=song.type_id,
            duration=song.duration,
            album_title=album.title,
            album_id=song.album_id,
            artist_name=artist.artist_name,
            artist_id=song.artist.artist_id
        ))
    return list

def convert_song_output(db: Session,song : Song) -> songOutput:
    album = get_album_by_id(db, song.album_id)
    artist = get_artist_by_id(db,album.artist_id)
    return songOutput(
            song_id=song.song_id,
            title=song.title,
            type=song.type_id,
            duration=song.duration,
            album_title=album.title,
            album_id=song.album_id,
            artist_name=artist.artist_name,
            artist_id=album.artist_id
        )
def convert_song_create_to_song(album : Album_Model, schema: songCreate)-> Song:
    return Song(
            title=schema.title,
            artist_id=album.artist_id,
            duration=schema.duration,
            type_id=schema.type,
            album_id=album.album_id,
            updated_at=datetime.utcnow(),  
            deleted_at=None,
        )