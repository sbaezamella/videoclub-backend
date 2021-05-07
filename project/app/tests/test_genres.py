from datetime import datetime

from starlette.testclient import TestClient
from app.crud import genres


url = "/api/v1"


def test_get_all_genres(client: TestClient):
    response = client.get(f"{url}/genres/")
    assert response.status_code == 200


def test_create_genre(client: TestClient, monkeypatch):
    test_request_payload = {
        "name": "something",
    }

    datetime_now = datetime.utcnow().isoformat()
    test_response_payload = {
        "id": 1,
        "name": "something",
        "created_at": datetime_now,
        "updated_at": datetime_now,
    }

    async def mock_post(payload):
        return test_response_payload

    monkeypatch.setattr(genres, "post", mock_post)

    response = client.post(
        f"{url}/genres/",
        json=test_request_payload,
    )

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_get_genre(client: TestClient, monkeypatch):
    datetime_now = datetime.utcnow().isoformat()
    test_data = {
        "id": 1,
        "name": "something",
        "created_at": datetime_now,
        "updated_at": datetime_now,
    }

    async def mock_get(genre_id):
        return test_data

    monkeypatch.setattr(genres, "get", mock_get)

    response = client.get(f"{url}/genres/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_update_genre(client: TestClient, monkeypatch):
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

    monkeypatch.setattr(genres, "put", mock_put)

    response = client.put(
        f"{url}/1/",
        json=test_request_payload,
    )
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_delete_genre(client: TestClient, monkeypatch):
    async def mock_get(id):
        return {
            "id": 1,
            "url": "https://foo.bar",
            "summary": "summary",
            "created_at": datetime.utcnow().isoformat(),
        }

    monkeypatch.setattr(genres, "get", mock_get)

    async def mock_delete(id):
        return None

    monkeypatch.setattr(genres, "delete", mock_delete)

    response = client.delete(f"{url}/1/")
    assert response.status_code == 204
    assert response.json() == {"id": 1, "url": "https://foo.bar"}
