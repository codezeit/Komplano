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
        # "id": 1,
        "title": "Clean Toilet",
        "description": "Make sure everything is clean",
        "room": "Bathroom",
        "cycle_days": 7,
        "flat_id": 1
        }
    print(test_chore)
    response = client.post("/chores/", json=test_chore)
    print(response)
    assert response.status_code == 200


def test_chore_done():
    """
    Test user marking a chore as done. This should be written
    to the chore log table.
    """
    
    # chore_id = id of chore user marks as done
    
    # user_id = id of user (currently logged in user)
    # who marks the chore as done
    
    response = client.post(f"/chores/{chore_id}")
    assert response.status_code == 200
