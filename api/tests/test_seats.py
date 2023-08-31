
from fastapi.testclient import TestClient
from main import app
from queries.seats import SeatsQueries


client = TestClient(app)


class EmptySeatsQueries:
    def get_reserved_seats(self):
        return []


class CreateSeatQueries:
    def create_reserved(self, reserved):
        result = {
            "id": 23,
            "showtime_id": 24,
            "user_id": 25,
            "available": True,
            "seat_id": "Z19"
        }
        result.update(reserved)
        return result


def test_get_reserved():
    app.dependency_overrides[SeatsQueries] = EmptySeatsQueries

    response = client.get("/seats")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {"reserved": []}


def test_create_reserved():
    app.dependency_overrides[SeatsQueries] = CreateSeatQueries
    json = {
        "id": 23,
        "showtime_id": 24,
        "user_id": 25,
        "available": True,
        "seat_id": "Z19"
    }
    expected = {
        "id": 23,
        "showtime_id": 24,
        "user_id": 25,
        "available": True,
        "seat_id": "Z19"
    }
    response = client.post("/seats", json=json)

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected
