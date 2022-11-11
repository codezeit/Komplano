"""Test /users routes."""

from fastapi.testclient import TestClient
# from fastapi import Form
from ..db.database import Base, get_engine
from ..main import app
from .fixtures import test_users
import pytest

@pytest.fixture()
def drop_and_create_db():
    Base.metadata.drop_all(bind=get_engine())
    Base.metadata.create_all(bind=get_engine())


client = TestClient(app)


def test_login_no_user(drop_and_create_db):
    drop_and_create_db()
    """Test Post /auth/login route."""
    test_user = test_users["test_user1"]
    response = client.post("/auth/login", data={
        "username": test_user["username"],
        "password": test_user["password"]
    })
    print(response.content)
    assert response.status_code == 401


def test_login(drop_and_create_db):
    drop_and_create_db()
    """Test Post /auth/login route."""
    test_user = test_users["test_user3"]
    response = client.post("/users/", json=test_user)
    assert response.status_code == 200
    response = client.post("/auth/login", data={
        "username": test_user["username"],
        "password": test_user["password"]
        })
    print(response.content)
    assert response.status_code == 200
