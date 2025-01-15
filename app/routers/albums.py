from fastapi import APIRouter, Depends, HTTPException
from ..models.Albums.service import get_album_by_id, get_albums
from ..models.Albums.schemas import AlbumOutput
from typing import List
from sqlalchemy.orm import Session
from uuid import UUID
from ..core.database import get_db
router = APIRouter(
    prefix="/api", 
    tags=["albums"],
)

@router.get("/albums",response_model=List[AlbumOutput])
async def get_all_albums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_albums(db, skip=skip, limit=limit)

@router.get("/albums/{id}",response_model=AlbumOutput)
async def get_albums_id(id : UUID, db: Session = Depends(get_db)):
    album =  get_album_by_id(db,id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.post("/albums")
async def get_all_albums():
    return {"message": "all albums"}

@router.put("/artist/{id}")
async def get_song_by_id(id : int):
    return {"modification artist": id}

@router.put("/albums/{id}")
async def get_song_by_id(id : int):
    return {"modification album": id}

@router.delete("/albums/{id}")
async def get_song_by_id(id : int):
    return {"delete album": id}

@router.delete("/artist/{id}")
async def get_song_by_id(id : int):
    return {"delete artist": id}