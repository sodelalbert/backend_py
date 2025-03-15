from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_count": 544,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "published_date": "2020-11-15",
        "page_count": 592,
        "language": "English",
    },
]


app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModule(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


@app.get("/books", response_model=list[Book])
async def get_all_books() -> list:
    return books


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK, response_model=Book)
async def get_book_by_id(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@app.patch("/books/{book_id}", status_code=status.HTTP_200_OK, response_model=Book)
async def update_book(book_id: int, book_update_data: BookUpdateModule) -> dict:
    for book in books:
        if book["id"] == book_id:
            book.update(book_update_data.model_dump())
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_200_OK, response_model=dict)
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
