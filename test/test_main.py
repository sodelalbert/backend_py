import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.mark.asyncio
async def test_read_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_greet():
    client = TestClient(app)
    response = client.get("/greet/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John"}
