from pydantic import BaseModel
from queries.pool import pool
from fastapi import HTTPException
from typing import List


class Error(BaseModel):
    message: str


class SeatsReserved(BaseModel):
    id: int
    showtime_id: int
    user_id: int
    available: bool
    seat_id: str


class ReservedOut(BaseModel):
    id: int
    showtime_id: int
    user_id: int
    available: bool
    seat_id: str


class ReservedIn(BaseModel):
    showtime_id: int
    user_id: int
    seat_id: List[str]


class SeatsQueries:
    def get_reserved_seats(self):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            SELECT id,
                            showtime_id,
                            user_id,
                            available,
                            seat_id
                            FROM reserved_seats
                            """
                    )
                    records = db.fetchall()
                    if len(records) == 0:
                        return []
                    else:
                        return [
                            ReservedOut(
                                id=record[0],
                                showtime_id=record[1],
                                user_id=record[2],
                                available=record[3],
                                seat_id=record[4],
                            )
                            for record in records
                        ]
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))

    def create_reserved(self, reserved: SeatsReserved):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    seat_ids = reserved.seat_id
                    reserved_out_list = []
                    for seat_id in seat_ids:
                        db.execute(
                            """
                            INSERT INTO reserved_seats
                                (
                                showtime_id,
                                user_id,
                                available,
                                seat_id
                                )
                            VALUES
                                (%s, %s, %s, %s)
                            RETURNING id,
                            showtime_id,
                            user_id,
                            available,
                            seat_id
                            """,
                            [
                                reserved.showtime_id,
                                reserved.user_id,
                                False,
                                seat_id,
                            ],
                        )
                        record = db.fetchone()
                        reserved_out_list.append(
                            ReservedOut(
                                id=record[0],
                                showtime_id=record[1],
                                user_id=record[2],
                                available=record[3],
                                seat_id=record[4],
                            )
                        )
                    return reserved_out_list
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))
