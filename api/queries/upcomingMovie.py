from pydantic import BaseModel
from typing import List
from queries.pool import pool
import json


class UpcomingMovie(BaseModel):
    id: int
    title: str
    description: str
    image: str
    trailer: str


class UpcomingMoviesQueries:
    def get_one(self, id: int) -> UpcomingMovie:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id,
                           title,
                           description,
                           image,
                           trailer
                    FROM upcoming_movies
                    WHERE id = %s;
                    """,
                    [id],
                )
                record = result.fetchone()
                print(record)
                movie = UpcomingMovie(
                    id=record[0],
                    title=record[1],
                    description=record[2],
                    image=record[3],
                    trailer=json.dumps(record[4]),  # Convert to JSON string
                )
                return movie

    def get_all(self) -> List[UpcomingMovie]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                          SELECT id,
                          title,
                          description,
                          image,
                          trailer
                          FROM upcoming_movies
                          """
                )
                movies = []
                for record in result:
                    movie = UpcomingMovie(
                        id=record[0],
                        title=record[1],
                        description=record[2],
                        image=record[3],
                        trailer=str(record[4]),
                    )
                    movies.append(movie)
                return movies

    def delete_one(self, id: int):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM upcoming_movies
                    WHERE id = %s;
                    """,
                    [id],
                )
