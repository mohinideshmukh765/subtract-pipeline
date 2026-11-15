import pytest
from fastapi.testclient import TestClient
from subtract import subtract
from main import app

client = TestClient(app)


@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 5),
    (5, 10, -5),
    (0, 0, 0),
    (-3, -7, 4),
    (5.5, 2.5, 3.0),
])
def test_subtract_function(a, b, expected):
    assert subtract(a, b) == expected


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_subtract_api():
    response = client.get("/subtract", params={"a": 20, "b": 8})
    assert response.status_code == 200
    assert response.json()["result"] == 12


def test_invalid_input():
    response = client.get("/subtract", params={"a": "abc", "b": 5})
    assert response.status_code == 422