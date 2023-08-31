
from fastapi.testclient import TestClient
from main import app
from queries.showtimes import ShowtimeRepository


client = TestClient(app)


class EmptyShowtimesQueries:
    def get_all(self):
        return []


def test_get_all_showtimes():
    app.dependency_overrides[ShowtimeRepository] = EmptyShowtimesQueries

    response = client.get("/api/showtimes")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {"showtimes": []}
