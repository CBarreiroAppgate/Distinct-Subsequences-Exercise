import pytest
from fastapi.testclient import TestClient

from app.infrastructure.app_factory import create_app


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(create_app())


class TestSubsequencesEndpoint:
    def test_count_subsequences_returns_correct_count(self, client: TestClient):
        response = client.post("/subsequences", json={"source": "rabbbit", "target": "rabbit"})
        assert response.status_code == 200
        assert response.json() == {"count": 3}

    def test_target_longer_than_source_returns_zero(self, client: TestClient):
        response = client.post("/subsequences", json={"source": "ab", "target": "abc"})
        assert response.status_code == 200
        assert response.json() == {"count": 0}

    def test_invalid_source_returns_422(self, client: TestClient):
        response = client.post("/subsequences", json={"source": "abc123", "target": "abc"})
        assert response.status_code == 422
        body = response.json()
        assert "detail" in body
        assert body["detail"][0]["field"] == "input"

    def test_empty_source_returns_422(self, client: TestClient):
        response = client.post("/subsequences", json={"source": "", "target": "abc"})
        assert response.status_code == 422


class TestEventSubsequencesEndpoint:
    def test_count_event_subsequences_returns_correct_count(self, client: TestClient):
        source = ["LOGIN", "ADD_TO_CART", "CHECKOUT", "ADD_TO_CART", "CHECKOUT"]
        target = ["ADD_TO_CART", "CHECKOUT"]
        response = client.post("/event-subsequences", json={"source": source, "target": target})
        assert response.status_code == 200
        assert response.json()["count"] > 0

    def test_invalid_event_token_returns_422(self, client: TestClient):
        response = client.post(
            "/event-subsequences",
            json={"source": ["LOGIN", "invalid token!"], "target": ["LOGIN"]},
        )
        assert response.status_code == 422
        body = response.json()
        assert "detail" in body
        assert body["detail"][0]["field"] == "input"

    def test_empty_event_list_returns_422(self, client: TestClient):
        response = client.post("/event-subsequences", json={"source": [], "target": ["LOGIN"]})
        assert response.status_code == 422