"""Test routes in main.py."""

from fastapi.testclient import TestClient
from ..db.database import Base, get_engine
from ..main import app

Base.metadata.drop_all(bind=get_engine())
Base.metadata.create_all(bind=get_engine())

client = TestClient(app)

test_user_dict = {
        "email": "foo@bar.com",
        "name": "Foo Bar",
        "id": 1
    }


def test_get_users():
    """Test GET /users route."""
    response = client.get("/users")
    assert response.status_code == 200


def test_create_user():
    """Test POST /users route."""
    response = client.post("/users/", json={
        "email": test_user_dict["email"],
        "name": test_user_dict["name"],
        "password": "foobar"
    })
    assert response.status_code == 200
    user = response.json()
    assert user == test_user_dict
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json()[0] == user
    

def test_create_user_duplicate_email():
    """Test POST /users route with duplicate email."""
    response = client.post("/users/", json={
        "email": "foo@bar.com",
        "name": "Bare Foot",
        "password": "barefoot"
    })
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Email already registered"
    }


def test_get_users_filled():
    """Test GET /users route."""
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [
            test_user_dict
        ]
