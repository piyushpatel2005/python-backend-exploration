from fastapi import APIRouter

router = APIRouter()

authors = [
    {"author_id": 1, "name": "F. Scott Fitzgerald"},
    {"author_id": 2, "name": "Fyodor Dostoevsky"},
    {"author_id": 3, "name": "J.R.R. Tolkien"},
    {"author_id": 4, "name": "Harper Lee"},
]

@router.get("/")
async def read_authors():
    return authors

@router.get("/{author_id}")
async def read_author(author_id: int):
    return authors[author_id]