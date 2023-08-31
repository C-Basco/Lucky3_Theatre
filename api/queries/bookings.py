from pydantic import BaseModel
from queries.pool import pool
from typing import List, Optional
from fastapi import HTTPException


class Error(BaseModel):
    message: str


class Booking(BaseModel):
    id: int
    showtime_id: int
    reserved_seat_id: int
    user_id: int
    confirmation_code: str


class BookingIn(BaseModel):
    showtime_id: int
    reserved_seat_id: List[int]
    user_id: int
    confirmation_code: str


class BookingOut(BaseModel):
    id: int
    showtime_id: int
    reserved_seat_id: int
    user_id: int
    confirmation_code: str


class BookingsQueries:
    def create_booking(self, booking_data: BookingIn):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    seat_ids = booking_data.reserved_seat_id
                    bookings = []
                    for reserved_seat_id in seat_ids:
                        db.execute(
                            """
                            INSERT INTO bookings (
                                showtime_id,
                                reserved_seat_id,
                                user_id,
                                confirmation_code)
                            VALUES (%s, %s, %s, %s)
                            RETURNING id,
                            showtime_id,
                            reserved_seat_id,
                            user_id,
                            confirmation_code;
                        """,
                            [
                                booking_data.showtime_id,
                                reserved_seat_id,
                                booking_data.user_id,
                                booking_data.confirmation_code,
                            ],
                        )
                        record = db.fetchone()
                        bookings.append(
                            Booking(
                                id=record[0],
                                showtime_id=record[1],
                                reserved_seat_id=record[2],
                                user_id=record[3],
                                confirmation_code=record[4],
                            )
                        )
                    return bookings
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))

    def get_all_bookings(self):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id,
                        showtime_id,
                        reserved_seat_id,
                        user_id,
                        confirmation_code
                        FROM bookings
                    """
                    )
                    records = db.fetchall()
                    if len(records) == 0:
                        return []
                    else:
                        return [
                            BookingOut(
                                id=record[0],
                                showtime_id=record[1],
                                reserved_seat_id=record[2],
                                user_id=record[3],
                                confirmation_code=record[4],
                            )
                            for record in records
                        ]
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))

    def get_booking_by_id(self, booking_id: int) -> Optional[Booking]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id,
                    showtime_id,
                    reserved_seat_id,
                    user_id,
                    confirmation_code
                    FROM bookings
                    WHERE id = %s
                """,
                    [booking_id],
                )
                record = db.fetchone()
                if record:
                    booking = Booking(
                        id=record[0],
                        showtime_id=record[1],
                        reserved_seat_id=record[2],
                        user_id=record[3],
                        confirmation_code=record[4],
                    )
                    return booking
                else:
                    return None

    def get_booking_by_user_id(self, user_id: int) -> List[BookingOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id,
                        showtime_id,
                        reserved_seat_id,
                        user_id,
                        confirmation_code
                        FROM bookings
                        WHERE user_id = %s
                        """,
                        [user_id],
                    )
                    records = db.fetchall()
                    return [
                        BookingOut(
                            id=record[0],
                            showtime_id=record[1],
                            reserved_seat_id=record[2],
                            user_id=record[3],
                            confirmation_code=record[4],
                        )
                        for record in records
                    ]
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))
