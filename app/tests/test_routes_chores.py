"""Test /users routes."""

from fastapi.testclient import TestClient
from ..db.database import Base, get_engine
from ..main import app
from .fixtures import test_users
from ..crud.crud import get_user_by_email

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

    # Create user
    user = test_users["test_user4"]
    response_user = client.post("/users/", json=user)
    print(response_user.status_code, response_user.json())
    
    # Create chore
    chore = {"title": "Testchore",
             "description": "Test description",
             "room": "test room"}
    response_chore = client.post("/chores/", json=chore)
    print(response_chore.status_code, response_chore.json())
    
    # Login user
    username = user["email"]
    password = user["password"]
    response_login = client.post("/auth/login", data={
        "username": username,
        "password": password
        })
    
    token_info = response_login.json()
    access_token = token_info["access_token"]
    token_type = token_info["token_type"]
    auth_header = {
        "Authorization": f"{token_type} {access_token}"
    }
    print('auth header: ', auth_header)

    # Mark chore as done
    chore_id = 1
    response = client.post(f"/chores/{chore_id}",
                           headers=auth_header,
                           json={"finished": True})
    print(response.status_code, response.content)
    assert response.status_code == 200
