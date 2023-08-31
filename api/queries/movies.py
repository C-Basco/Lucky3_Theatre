from pydantic import BaseModel
from typing import List
from queries.pool import pool
import json


class Movie(BaseModel):
    id: int
    title: str
    description: str
    image: str
    trailer: str


class MoviesQueries:
    def get_one(self, id: int) -> Movie:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT id,
                           title,
                           description,
                           image,
                           trailer
                    FROM movies
                    WHERE id = %s;
                    """,
                    [id],
                )
                record = result.fetchone()
                print(record)
                movie = Movie(
                    id=record[0],
                    title=record[1],
                    description=record[2],
                    image=record[3],
                    trailer=json.dumps(record[4]),  # Convert to JSON string
                )
                return movie

    def get_all(self) -> List[Movie]:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                          SELECT id,
                          title,
                          description,
                          image,
                          trailer
                          FROM movies
                          """
                )
                movies = []
                for record in result:
                    movie = Movie(
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
                    DELETE FROM movies
                    WHERE id = %s;
                    """,
                    [id],
                )
