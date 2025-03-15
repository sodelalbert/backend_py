from fastapi.testclient import TestClient
from app.main import app
from app.main import books
import pytest


client = TestClient(app)


@pytest.mark.asyncio
async def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) == len(books)


@pytest.mark.asyncio
async def test_get_book_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


@pytest.mark.asyncio
async def test_get_book_by_id_not_found():
    response = client.get("/books/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}


@pytest.mark.asyncio
async def test_create_book():
    new_book = {
        "id": 4,
        "title": "New Book",
        "author": "New Author",
        "publisher": "New Publisher",
        "published_date": "2023-01-01",
        "page_count": 100,
        "language": "English",
    }
    response = client.post("/books", json=new_book)
    assert response.status_code == 201
    assert response.json() == new_book


@pytest.mark.asyncio
async def test_create_book_with_existing_id():
    new_book = {
        "id": 5,
        "title": "Duplicate Book",
        "author": "Duplicate Author",
        "publisher": "Duplicate Publisher",
        "published_date": "2023-01-01",
        "page_count": 100,
        "language": "English",
    }
    client.post("/books", json=new_book)
    response = client.post("/books", json=new_book)
    assert response.status_code == 400
    assert response.json() == {"detail": "Book with this ID already exists"}


@pytest.mark.asyncio
async def test_update_book():
    updated_data = {
        "title": "Updated Title",
        "author": "Updated Author",
        "publisher": "Updated Publisher",
        "page_count": 200,
        "language": "English",
    }
    response = client.patch("/books/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


@pytest.mark.asyncio
async def test_update_book_not_found():
    updated_data = {
        "title": "Updated Title",
        "author": "Updated Author",
        "publisher": "Updated Publisher",
        "page_count": 200,
        "language": "English",
    }
    response = client.patch("/books/999", json=updated_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}


@pytest.mark.asyncio
async def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Book deleted"}


@pytest.mark.asyncio
async def test_delete_book_not_found():
    response = client.delete("/books/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}
