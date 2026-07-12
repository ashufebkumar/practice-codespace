from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "User endpoint is working"}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_not_found_returns_json_error():
    response = client.get("/does-not-exist")
    assert response.status_code == 404
    assert "detail" in response.json()


def test_lifespan_sets_app_state():
    with TestClient(app) as client:
        assert client.app.state.started is True
        assert client.app.state.resource.initialized is True

    assert app.state.started is False
    assert app.state.resource.initialized is False


def test_items_endpoints_work_with_sqlalchemy():
    create_response = client.post("/items", json={"name": "sample"})
    assert create_response.status_code == 201

    list_response = client.get("/items")
    assert list_response.status_code == 200
    assert any(item["name"] == "sample" for item in list_response.json())