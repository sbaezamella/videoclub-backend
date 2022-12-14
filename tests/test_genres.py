from datetime import datetime
from typing import List

from starlette.testclient import TestClient

from app.crud import crud_genre
from app.core.config import settings

url = settings.api_v1_str


def test_get_all_genres(client: TestClient, monkeypatch) -> None:
    mocked_response = []

    async def mock_get_all() -> List:
        return mocked_response

    monkeypatch.setattr(crud_genre, "get_all", mock_get_all)

    response = client.get(f"{url}/genres/")

    assert response.status_code == 200
    assert response.json() == mocked_response


def test_create_genre(client: TestClient, monkeypatch) -> None:
    test_request_payload = {
        "name": "something",
    }

    datetime_now = datetime.now().isoformat()
    test_response_payload = {
        "id": 1,
        "name": "something",
        "created_at": datetime_now,
        "updated_at": datetime_now,
    }

    async def mock_post(payload):
        return test_response_payload

    monkeypatch.setattr(crud_genre, "post", mock_post)

    response = client.post(
        f"{url}/genres/",
        json=test_request_payload,
    )

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_get_genre(client: TestClient, monkeypatch) -> None:
    datetime_now = datetime.utcnow().isoformat()
    test_data = {
        "id": 1,
        "name": "something",
        "created_at": datetime_now,
        "updated_at": datetime_now,
    }

    async def mock_get(genre_id):
        return test_data

    monkeypatch.setattr(crud_genre, "get", mock_get)

    response = client.get(f"{url}/genres/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_get_genre_not_found(client: TestClient, monkeypatch) -> None:
    async def mock_get(genre_id):
        return None

    monkeypatch.setattr(crud_genre, "get", mock_get)

    response = client.get(f"{url}/genres/999")
    assert response.status_code == 404
    assert response.json().get("detail") == "Genre not found"


def test_update_genre(client: TestClient, monkeypatch) -> None:
    datetime_now = datetime.utcnow().isoformat()
    test_request_payload = {
        "name": "something",
    }
    test_response_payload = {
        "id": 1,
        "name": "something",
        "created_at": datetime_now,
        "updated_at": datetime_now,
    }

    async def mock_put(id, payload):
        return test_response_payload

    monkeypatch.setattr(crud_genre, "put", mock_put)

    response = client.put(
        f"{url}/genres/1",
        json=test_request_payload,
    )
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_update_genre_not_found(client: TestClient, monkeypatch) -> None:
    test_request_payload = {
        "name": "something",
    }

    async def mock_put(id, payload):
        return None

    monkeypatch.setattr(crud_genre, "put", mock_put)

    response = client.put(
        f"{url}/genres/999",
        json=test_request_payload,
    )
    assert response.status_code == 404
    assert response.json().get("detail") == "Genre not found"


def test_update_genre_name_taken(client: TestClient, monkeypatch) -> None:
    # TODO: create test for name taken
    assert True == False


def test_delete_genre(client: TestClient, monkeypatch) -> None:
    async def mock_delete(id):
        return 1  # deleted count, 1 if found else 0

    monkeypatch.setattr(crud_genre, "delete", mock_delete)

    response = client.delete(f"{url}/genres/1")
    assert response.status_code == 204


def test_delete_genre_not_found(client: TestClient, monkeypatch) -> None:
    async def mock_delete(id):
        return 0  # deleted count, 1 if found else 0

    monkeypatch.setattr(crud_genre, "delete", mock_delete)

    response = client.delete(f"{url}/genres/999")
    assert response.status_code == 404
    assert response.json().get("detail") == "Genre not found"
