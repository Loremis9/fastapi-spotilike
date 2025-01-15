from fastapi import APIRouter, Depends, HTTPException
from ..core.dependencies import get_token_header

router = APIRouter(
    prefix="/api",
    tags=["songs"]
)

@router.get("/artist/{id}/songs")
async def get_all_song_by_artist_id(id : int):
    return {"song by artist_id": id}

@router.get("/albums/{id}/songs")
async def get_song_by_id(id : int):
    return {"song by id": id}

@router.post("/albums/{id}/songs")
async def get_song_by_id(id : int):
    return {"song by id post": id}

@router.get("/genres")
async def get_all_genre():
    return {"genre": ["genre"]}

@router.put("api/genre/{id}")
async def get_song_by_id(id : int):
    return {"modification genre": id}

@router.delete("/genre/{id}")
async def get_song_by_id(id : int):
    return {"delete genre": id}