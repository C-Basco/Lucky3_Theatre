from fastapi import APIRouter, Depends
from queries.upcomingMovie import UpcomingMovie, UpcomingMoviesQueries
from typing import List

router = APIRouter()


@router.get("/upcoming_movies/{id}", response_model=UpcomingMovie)
def get_one(id: int, repo: UpcomingMoviesQueries = Depends()) -> UpcomingMovie:
    return repo.get_one(id)


@router.get("/upcoming_movies", response_model=List[UpcomingMovie])
def get_all(repo: UpcomingMoviesQueries = Depends()) -> List[UpcomingMovie]:
    return repo.get_all()


@router.delete("/upcoming_movies/{id}")
def delete_one(id: int, repo: UpcomingMoviesQueries = Depends()):
    repo.delete_one(id)
    return {"message": "Movie deleted"}
