"""Test /users routes."""

from fastapi.testclient import TestClient
from ..db.database import Base, get_engine
from ..main import app

Base.metadata.drop_all(bind=get_engine())
Base.metadata.create_all(bind=get_engine())

client = TestClient(app)

test_users = {
    "test_user1": {
        "email": "foo@bar.com",
        "username": "Foo Bar",
        "password": "foobar",
    },
    "test_user2": {
        "email": "foo@bar.com",
        "username": "Bare Foot",
        "password": "barefoot",
    },
}


def compare_user_info(test_user, response_user):
    """Check if test user info equals database user info."""
    for key, value in response_user.items():
        if key in test_user.keys():
            if value != test_user[key]:
                return False
    return True


def test_get_users():
    """Test GET /users route."""
    response = client.get("/users")
    assert response.status_code == 200


def test_create_user():
    """Test POST /users route."""
    test_user = test_users["test_user1"]
    response = client.post("/users/", json=test_user)
    assert response.status_code == 200
    response_user = response.json()
    assert compare_user_info(test_user, response_user)

    # check if created user is really in db, this means also testing getting user by id
    response = client.get(f"/users/{response_user['id']}")
    assert response.status_code == 200
    response_user = response.json()
    assert compare_user_info(test_user, response_user)


def test_create_user_duplicate_email():
    """Test POST /users route with duplicate email."""
    test_user = test_users["test_user2"]
    response = client.post("/users/", json=test_user)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Email already registered"
    }


def test_get_users_filled():
    """Test GET /users route."""
    test_user = test_users["test_user1"]
    response = client.get("/users")
    assert response.status_code == 200
    assert compare_user_info(test_user, response.json()[0])
