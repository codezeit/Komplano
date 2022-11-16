"""Test /users routes."""

from fastapi.testclient import TestClient
from ..db.database import Base, get_engine
from ..main import app
# from .fixtures import test_users

Base.metadata.drop_all(bind=get_engine())
Base.metadata.create_all(bind=get_engine())


client = TestClient(app)


def test_get_chores():
    """Test GET /chores route"""
    response = client.get("/chores")
    print(response)
    assert response.status_code == 200


def test_create_chore():
    """Test POST /chores route"""
    test_chore = {
        "title": "Clean Toilet",
        "description": "Make sure everything is clean",
        # "room": "Bathroom",
        # "cycle_days": 7,
        # "flat_id": 1
        }
    print(type(test_chore))
    print(test_chore)
    response = client.post("/chores/", json=test_chore)
    print(response)
    print(response.headers)
    print(response.content)
    assert response.status_code == 200
