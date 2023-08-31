from fastapi import APIRouter, Depends, HTTPException
from queries.rooms import Rooms, RoomsQueries
from typing import List

router = APIRouter()


@router.get("/rooms", response_model=List[Rooms])
def get_all_rooms(repo: RoomsQueries = Depends()):
    return repo.get_rooms()


@router.get("/rooms/{room_id}", response_model=Rooms)
def get_room_by_id(room_id: int, repo: RoomsQueries = Depends()):
    room = repo.get_room_by_id(room_id)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


@router.post("/rooms", response_model=Rooms)
def create_room(room_data: Rooms, repo: RoomsQueries = Depends()):
    return repo.create_room(room_data)
