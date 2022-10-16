from typing import Optional

from fastapi import FastAPI
from enum import Enum

app = FastAPI()


BOOKS = {
    'book_1': {
        'title': 'Title one',
        'author': 'Author one'
    },
    'book_2': {
        'title': 'Title two',
        'author': 'Author two'
    },
    'book_3': {
        'title': 'Title three',
        'author': 'Author three'
    },
    'book_4': {
        'title': 'Title four',
        'author': 'Author four'
    },
    'book_5': {
        'title': 'Title five',
        'author': 'Author five'
    },
}


@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/{book_name}")
async def get_book(book_name: str):
    return BOOKS[book_name]


