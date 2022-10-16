from fastapi import FastAPI

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
async def read_all_books():
    return BOOKS

