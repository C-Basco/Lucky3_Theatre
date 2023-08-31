from fastapi import APIRouter, Depends
from queries.movies import Movie, MoviesQueries
from typing import List

router = APIRouter()


@router.get("/movies/{id}", response_model=Movie)
def get_one(id: int, repo: MoviesQueries = Depends()) -> Movie:
    return repo.get_one(id)


@router.get("/movies", response_model=List[Movie])
def get_all(repo: MoviesQueries = Depends()) -> List[Movie]:
    return repo.get_all()


@router.delete("/movies/{id}")
def delete_one(id: int, repo: MoviesQueries = Depends()):
    repo.delete_one(id)
    return {"message": "Movie deleted"}
