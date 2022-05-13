from typing import Generator

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["app.models.genres"])
    with TestClient(app) as c:
        yield c
    finalizer()
