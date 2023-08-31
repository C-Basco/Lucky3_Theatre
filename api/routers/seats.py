from fastapi import APIRouter, Depends
from queries.seats import SeatsQueries, ReservedOut, ReservedIn
from typing import List

router = APIRouter()


@router.get("/seats", response_model=List[ReservedOut])
def get_reserved(repo: SeatsQueries = Depends()):
    return repo.get_reserved_seats()


@router.post("/res_seats", response_model=List[ReservedOut])
def create_reserved(reserved: ReservedIn, repo: SeatsQueries = Depends()):
    return repo.create_reserved(reserved)
