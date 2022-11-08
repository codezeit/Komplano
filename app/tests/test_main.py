"""Test routes in main.py. You need to have requests and pytest installed."""

from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_users_route():
    """Test GET /users route."""
    response = client.get("/users")
    assert response.status_code == 200
