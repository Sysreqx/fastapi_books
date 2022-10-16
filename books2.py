from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


BOOKS = []


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                       max_length=100,
                                       min_length=1)
    rating: int = Field(gt=-1, lt=101)

    class Config:

        schema_extra = {
            "example": {
                "id": "7f644f5f-3fc0-4923-9a5a-782a38457c91",
                "title": "Computer Science Pro",
                "author": "Kaisar",
                "description": "A very nice description ov a book",
                "rating": 80
            }
        }


@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_book_no_api()

    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books

    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for b in BOOKS:
        if b.id == book_id:
            return b


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book


def create_book_no_api():
    book_1 = Book(id='7f644f5f-3fc0-4920-9a5a-782a38457c91',
                  title='Title 1',
                  author='Author 1',
                  description='Description 1',
                  rating=60)
    book_2 = Book(id='baa52f64-881f-4684-bb33-74159baaeb76',
                  title='Title 2',
                  author='Author 2',
                  description='Description 2',
                  rating=70)
    book_3 = Book(id='a811c277-72f7-400f-b645-38057c7d8801',
                  title='Title 3',
                  author='Author 3',
                  description='Description 3',
                  rating=55)
    book_4 = Book(id='9bdae174-270a-4117-aa57-ad4a0ad4fc78',
                  title='Title 4',
                  author='Author 4',
                  description='Description 4',
                  rating=87)

    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
