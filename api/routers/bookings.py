from fastapi import APIRouter, Depends, HTTPException
from queries.bookings import Booking, BookingsQueries, BookingIn, BookingOut
from typing import List

router = APIRouter()


@router.post("/bookings", response_model=List[BookingOut])
def create_booking(
    booking_data: BookingIn,
    repo: BookingsQueries = Depends(),
):
    return repo.create_booking(booking_data)


@router.get("/bookings", response_model=List[BookingOut])
def get_all_bookings(repo: BookingsQueries = Depends()):
    return repo.get_all_bookings()


@router.get("/bookings/{booking_id}", response_model=Booking)
def get_booking(booking_id: int, repo: BookingsQueries = Depends()):
    return repo.get_booking_by_id(booking_id)


@router.get("/bookings/user/{user_id}", response_model=List[BookingOut])
def get_bookings_by_user_id(user_id: int, repo: BookingsQueries = Depends()):
    bookings = repo.get_booking_by_user_id(user_id)
    if not bookings:
        raise HTTPException(
            status_code=404, detail="Bookings not found for this user"
        )
    return bookings
