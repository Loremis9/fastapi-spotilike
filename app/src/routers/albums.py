from fastapi import APIRouter, Depends, HTTPException
from ..models.albums import service as service_album
from ..models.albums.schemas import AlbumOutput, AlbumCreate, AlbumModify
from ..models.artists.schemas import ArtistCreate, ArtistOutput, ArtistModify
from ..models.artists import service as service_artist
from typing import List
from sqlalchemy.orm import Session
from uuid import UUID
from ...core.database import get_db

router = APIRouter(
    prefix="", 
    tags=["albums"],
)

@router.get("/albums",response_model=List[AlbumOutput])
async def get_all_albums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    album = service_album.get_albums(db, skip=skip, limit=limit)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@router.get("/albums/{album_id}",response_model=AlbumOutput)
async def get_albums_id(album_id : UUID, db: Session = Depends(get_db)):
    album =  service_album.get_album_by_id(db,album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.post("/albums",response_model=AlbumOutput)
async def get_all_albums(schema:AlbumCreate, db: Session = Depends(get_db)):
    return service_album.create_album(db, schema)

@router.put("/artist/{artist_id}",response_model=ArtistOutput)
async def put_artist_by_id(artist_id : UUID, schema : ArtistModify , db: Session = Depends(get_db)):
    return service_artist.put_artist(artist_id, schema,db)

@router.put("/albums/{album_id}",response_model=AlbumOutput)
async def put_alubms_by_id(album_id : UUID,schema: AlbumModify, db: Session = Depends(get_db)):
    return service_album.put_album(db, album_id, schema)

@router.delete("/albums/{album_id}")
async def get_song_by_id(album_id : UUID, db: Session = Depends(get_db)):
    return service_album.remove_album(album_id, db)

@router.delete("/artist/{artist_id}")
async def get_song_by_id(artist_id : UUID, db: Session = Depends(get_db)):
    return service_artist.remove_album(artist_id)