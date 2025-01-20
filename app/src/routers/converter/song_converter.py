from ...models.songs.models import Song
from ...models.songs.schemas import songOutput,songCreate
from datetime import datetime
from ...models.albums.models import Album as Album_Model

def convert_songs_output(songs : Song):
    return [songOutput(
            song_id=song.song_id,
            title=song.title,
            type=song.type_id,
            duration=song.duration,
            album_id=song.album_id,
            artist_id=song.artist.artist_id
        ) for song in songs]

def convert_song_output(song : Song):
    return songOutput(
            song_id=song.song_id,
            title=song.title,
            type=song.type_id,
            duration=song.duration,
            album_id=song.album_id,
            artist_id=song.artist_id
        )
def convert_song_create_to_song(album : Album_Model, schema: songCreate):
    return Song(
            title=schema.title,
            artist_id=album.artist_id,
            duration=schema.duration,
            type_id=schema.type,
            album_id=album.album_id,
            updated_at=datetime.now(datetime.timezone.utc),  
            deleted_at=None,
        )