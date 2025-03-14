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
    response = client.get("/greet?name=John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John"}


@pytest.mark.asyncio
async def test_greet_no_name():
    client = TestClient(app)
    response = client.get("/greet?name=")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, "}


@pytest.mark.asyncio
async def test_greet_special_characters():
    client = TestClient(app)
    response = client.get("/greet?name=John%20Doe")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John Doe"}


@pytest.mark.asyncio
async def test_greet_numeric_name():
    client = TestClient(app)
    response = client.get("/greet?name=12345")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, 12345"}
