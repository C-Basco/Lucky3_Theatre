from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.showtimes import (
    ShowtimesIn,
    ShowtimeRepository,
    ShowtimeOut,
    Error,
)

router = APIRouter()


@router.post("/showtimes", response_model=Union[ShowtimeOut, Error])
def create_showtime(
    showtime: ShowtimesIn,
    repo: ShowtimeRepository = Depends(),
):
    return repo.create(showtime)


@router.get("/showtimes", response_model=List[ShowtimeOut])
def get_all(
    repo: ShowtimeRepository = Depends(),
):
    return repo.get_all()


@router.post(
    "/showtimes/{showtimes_id}", response_model=Union[Error, ShowtimeOut]
)
def update_showtimes(
    showtimes_id: int,
    showtimes: ShowtimesIn,
    repo: ShowtimeRepository = Depends(),
) -> Union[Error, ShowtimeOut]:
    repo.update(showtimes_id, showtimes)


@router.delete("/showtimes/{showtimes_id}", response_model=bool)
def delete_showtime(
    showtimes_id: int,
    repo: ShowtimeRepository = Depends(),
) -> bool:
    return repo.delete(showtimes_id)


@router.get("/showtimes/{showtimes_id}", response_model=Optional[ShowtimeOut])
def get_one_showtime(
    showtimes_id: int,
    repo: ShowtimeRepository = Depends(),
) -> ShowtimesIn:
    Response.status_code = 404
    return repo.get_one(showtimes_id)


@router.get("/movies/{movie_id}/showtimes", response_model=List[ShowtimeOut])
def get_showtimes_for_movie(
    movie_id: int,
    showtime_repo: ShowtimeRepository = Depends(),
):
    return showtime_repo.get_showtimes_for_movie(movie_id)
