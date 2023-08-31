from fastapi.testclient import TestClient
from routers.movies import router
from api.main import app
from queries.movies import Movie, MoviesQueries
from typing import List
import os
import sys


root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, root_path)


def test_get_one():
    client = TestClient(router)

    class FakeMoviesQueries:
        def get_one(self, id: int) -> Movie:
            return Movie(id=id, title="Test Movie")

    app.dependency_overrides[MoviesQueries] = FakeMoviesQueries()

    response = client.get("/movies/1")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Test Movie"}


def test_get_all():
    client = TestClient(router)

    class FakeMoviesQueries:
        def get_all(self) -> List[Movie]:
            return [Movie(id=1, title="Movie 1"), Movie(id=2, title="Movie 2")]

    app.dependency_overrides[MoviesQueries] = FakeMoviesQueries()

    response = client.get("/movies")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "Movie 1"},
        {"id": 2, "title": "Movie 2"},
    ]


def test_delete_one():
    client = TestClient(router)

    class FakeMoviesQueries:
        def delete_one(self, id: int):
            pass

    app.dependency_overrides[MoviesQueries] = FakeMoviesQueries()

    response = client.delete("/movies/1")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {"message": "Movie deleted"}
