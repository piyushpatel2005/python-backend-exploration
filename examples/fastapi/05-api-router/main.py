from fastapi import FastAPI
from books import router as books_router
from authors import router as authors_router

app = FastAPI()
app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(authors_router, prefix="/authors", tags=["authors"])

@app.get("/")
async def read_root():
    return {"message": "Hello World"}