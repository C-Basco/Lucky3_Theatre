from pydantic import BaseModel
from queries.pool import pool


class Error(BaseModel):
    message: str


class Rooms(BaseModel):
    id: int


class RoomsQueries:
    def get_rooms(self):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            SELECT id
                            FROM rooms
                        """
                    )
                    return [
                        Rooms(
                            id=record[0],
                        )
                        for record in db
                    ]
        except Exception as e:
            print(e)
            return Error(message="Could not retrieve rooms")

    def get_room_by_id(self, room_id):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            SELECT id
                            FROM rooms
                            WHERE id = %s
                        """,
                        (room_id,),
                    )
                    record = db.fetchone()
                    if record:
                        return Rooms(id=record[0])
                    else:
                        return None
        except Exception as e:
            print(e)
            return Error(message="Could not retrieve room")

    def create_room(self, room_data):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            INSERT INTO rooms (id)
                            VALUES (%s)
                        """,
                        (room_data.id,),
                    )
                    conn.commit()
                    return Rooms(id=room_data.id)
        except Exception as e:
            print(e)
            return Error(message="Could not create room")
