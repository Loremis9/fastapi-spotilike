from ...models.artists.models import Artist
from ...models.albums.models import Album
from ...models.albums.schemas import AlbumOutput
from ...models.artists.service import get_artist_by_id
from sqlalchemy.orm import Session


def convert_albums_output(db:Session,albums : Album) -> list[AlbumOutput]:
    album_list= []
    for album in albums:
        artist = get_artist_by_id(db,album.artist_id)
        album_list.append(AlbumOutput(
            album_id=album.album_id,
            title=album.title,
            pouch=album.pouch,
            release_date=album.release_date,
            artist_id = album.artist_id,
            artist_name=artist.artist_name))
    return album_list

def convert_album_output(db:Session, album : Album)-> AlbumOutput:
    artist = get_artist_by_id(db,album.artist_id)
    return AlbumOutput(
            album_id=album.album_id,
            title=album.title,
            pouch=album.pouch,
            release_date=album.release_date,
            artist_id = album.artist_id,
            artist_name=artist.artist_name
        )