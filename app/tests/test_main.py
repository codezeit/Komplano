"""Test routes in main.py. You need to have requests and pytest installed."""

from fastapi.testclient import TestClient

from ..main import app, get_db
from ..db.database import SessionLocalTest, Base, get_engine

client = TestClient(app)

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


def test_get_users():
    """Test GET /users route."""
    response = client.get("/users")
    assert response.status_code == 200


def test_create_user():
    """Test POST /users route."""
    response = client.post("/users/", json={
        "email": "foo@bar.com",
        "name": "Foo Bar",
        "password": "foobar"
    })
    assert response.status_code == 200
    user = response.json()
    assert user == {
        "email": "foo@bar.com",
        "name": "Foo Bar",
        "id": 1
    }

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

