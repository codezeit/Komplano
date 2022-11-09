"""Test routes in main.py. You need to have requests and pytest installed."""

from fastapi.testclient import TestClient

from ..main import app, get_db
from ..db.database import SessionLocalTest, Base, get_engine

client = TestClient(app)

Base.metadata.drop_all(bind=get_engine(test=True))
Base.metadata.create_all(bind=get_engine(test=True))


def override_get_db():
    """Overrides get_db function."""
    try:
        db = SessionLocalTest()
        yield db
    finally:
        db.close()


# Override get_db function
app.dependency_overrides[get_db] = override_get_db


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

    response = client.get(f"/users/{user['id']}")
    assert response.status_code == 200
    assert response.json() == user


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
