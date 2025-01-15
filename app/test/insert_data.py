import json
from datetime import datetime
from sqlalchemy.orm import Session
from ..models.types.models import Type
from ..models.Users.models import User, Role
from ..models.Artists.models import Artist
from ..models.Albums.models import Album
from ..models.Songs.models import Song
from ..models.Users.service import salt_password

# Fonction d'insertion des rôles et des utilisateurs
def insert_data_users_role(db: Session):
    json_file_path = "app/test/Set_data/users_roles_data.json"
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Insertion des rôles
    for role_data in data["roles"]:
        db_role = Role(role_id=role_data["role_id"], role_name=role_data["role_name"])
        db.add(db_role)
    db.commit()  
    print("Roles inserted.")
    # Insertion des utilisateurs
    for user_data in data["users"]:
        role = db.query(Role).filter(Role.role_id == user_data["role_id"]).first()
        db_user = User(
            user_id=user_data["user_id"],
            user_name=user_data["user_name"],
            mdp=salt_password(user_data["mdp"]),
            email=user_data["email"],
            age=user_data["age"],
            genre=user_data["genre"],
            role=role,
            updated_at=datetime.strptime(user_data["updated_at"], "%Y-%m-%d"),
            deleted_at=user_data["deleted_at"]
        )
        db.add(db_user)
    db.commit()
    print("Users inserted.")

# Fonction d'insertion des artistes
def insert_data_artists(db: Session):
    json_file_path = "app/test/Set_data/artists_data.json"
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Insertion des artistes
    for artist_data in data["artists"]:
        db_artist = Artist(
            artist_id=artist_data["artist_id"],
            artist_name=artist_data["artist_name"],
            avatar=artist_data["avatar"],
            biography=artist_data["biography"],
            updated_at=datetime.strptime(artist_data["updated_at"], "%Y-%m-%d"),
            deleted_at=artist_data["deleted_at"]
        )
        db.add(db_artist)

    db.commit()
    print("Artists inserted.")

# Fonction d'insertion des albums
def insert_data_albums(db: Session):
    json_file_path = "app/test/Set_data/albums_data.json"
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Insertion des albums
    for album_data in data["albums"]:
        artist = db.query(Artist).filter(Artist.artist_id == album_data["artist_id"]).first()
        released_at = datetime.strptime(album_data["release_date"], "%Y-%m-%d")
        db_album = Album(
            album_id=album_data["album_id"],
            title=album_data["title"],
            artist_id=artist.artist_id,
            pouch=album_data["pouch"],
            release_date=released_at,
            updated_at=datetime.strptime(album_data["updated_at"], "%Y-%m-%d"),
            deleted_at=album_data["deleted_at"]
        )
        db.add(db_album)
        
    db.commit()
    print("Albums inserted.")

# Fonction d'insertion des types
def insert_type_data(db: Session):
    json_file_path = "app/test/Set_data/types_data.json"
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Insertion des types
    for type_data in data["types"]:
        db_type = Type(
            type_id=type_data["type_id"],
            title=type_data["title"],
            description=type_data["description"],
            updated_at=datetime.strptime(type_data["updated_at"], "%Y-%m-%d"),
            deleted_at=type_data["deleted_at"]
        )
        db.add(db_type)

    db.commit()
    print("Types inserted.")

# Fonction d'insertion des morceaux (trackings)
def insert_songs_data(db: Session):
    json_file_path = "app/test/Set_data/songs_data.json"
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Insertion des morceaux
    for song_data in data["songs"]:
        artist = db.query(Artist).filter(Artist.artist_id == song_data["artist_id"]).first()
        album = db.query(Album).filter(Album.album_id == song_data["album_id"], Album.artist_id == artist.artist_id).first()
        db_song = Song(
            song_id=song_data["song_id"],
            title=song_data["title"],
            duration=song_data["duration"],
            artist_id=artist.artist_id,
            album_id=album.album_id,
            updated_at=datetime.strptime(song_data["updated_at"], "%Y-%m-%d"),
            deleted_at=song_data["deleted_at"]
        )
        db.add(db_song)

    db.commit()
    print("Songs inserted.")
