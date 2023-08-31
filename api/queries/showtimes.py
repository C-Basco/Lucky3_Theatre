from pydantic import BaseModel
from typing import Union, List
from queries.pool import pool


class Error(BaseModel):
    message: str


class ShowtimesIn(BaseModel):
    room_id: int
    movie_id: int
    time_slot: str


class ShowtimeOut(BaseModel):
    id: int
    room_id: int
    movie_id: int
    time_slot: str


class ShowtimeRepository:
    def get_one(self, showtime_id: int) -> ShowtimeOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id
                            ,room_id
                            ,movie_id
                            ,time_slot
                        FROM showtimes
                        WHERE id = %s;
                        """,
                        [showtime_id],
                    )
                    record = db.fetchone()
                    return self.record_to_showtime_out(record)
        except Exception as e:
            print(e)
            return Error(message="Could not retrieve showtimes")

    def delete(self, showtime_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM showtimes
                        WHERE id = %s
                        """,
                        [showtime_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(
        self, showtime_id: int, showtimes: ShowtimesIn
    ) -> Union[ShowtimeOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE showtimes
                        SET room_id = %s
                            ,movie_id = %s
                            ,time_slot=%s,
                        WHERE id = %s
                        """,
                        [
                            showtimes.room_id,
                            showtimes.movie_id,
                            showtimes.time_slot,
                            showtimes.id,
                        ],
                    )
                    return self.showtimes_in_to_out(showtime_id, showtimes)
        except Exception as e:
            print(e)
            return Error(message="Could not retrieve showtimes")

    def get_all(self) -> List[ShowtimeOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            SELECT id
                            ,room_id
                            ,movie_id
                            ,time_slot
                            FROM showtimes;
                        """
                    )
                    return [
                        ShowtimeOut(
                            id=record[0],
                            room_id=record[1],
                            movie_id=record[2],
                            time_slot=record[3],
                        )
                        for record in db.fetchall()
                    ]
        except Exception as e:
            print(e)
            return Error(message="Could not retrieve showtimes")

    def create(self, showtime: ShowtimesIn) -> ShowtimeOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        INSERT INTO showtimes
                            (room_id, movie_id, time_slot)
                        VALUES
                            (%s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            showtime.room_id,
                            showtime.movie_id,
                            showtime.time_slot,
                        ],
                    )
                    id = db.fetchone()[0]
                    return self.showtimes_in_to_out(id, showtime)
        except Exception as e:
            print(e)
            return Error(message="Could not create showtimes")

    def showtimes_in_to_out(self, id: int, showtime: ShowtimesIn):
        old_data = showtime.dict()
        return ShowtimeOut(id=id, **old_data)

    def record_to_showtime_out(self, record):
        return ShowtimeOut(
            id=record[0],
            room_id=record[1],
            movie_id=record[2],
            time_slot=record[3],
        )

    def get_showtimes_for_movie(self, movie_id: int) -> List[ShowtimeOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, room_id, movie_id, time_slot
                        FROM showtimes
                        WHERE movie_id = %s;
                        """,
                        [movie_id],
                    )
                    return [
                        ShowtimeOut(
                            id=record[0],
                            room_id=record[1],
                            movie_id=record[2],
                            time_slot=record[3],
                        )
                        for record in db.fetchall()
                    ]
        except Exception as e:
            print(e)
            return [Error(message="Could not retrieve showtimes")]
