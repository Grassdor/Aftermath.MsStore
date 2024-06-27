from fastapi.testclient import TestClient

from entry import app

client = TestClient(app)


def test_entry():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'store': "EVC Group"}


def test_accessory_get():
    response = client.get("/accessory")
    assert response.status_code == 200
    assert type(response.json()) == list
