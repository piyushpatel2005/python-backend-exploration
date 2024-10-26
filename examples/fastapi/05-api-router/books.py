from fastapi import APIRouter

router = APIRouter()

books = [
    {"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"book_id": 2, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
    {"book_id": 3, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"book_id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

@router.get("/")
async def read_books():
    return books

@router.get("/{book_id}")
async def read_book(book_id: int):
    return books[book_id - 1]