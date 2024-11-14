from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

class CustomException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "There was a server error"},
    )

@app.exception_handler(CustomException)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )

@app.get("/error")
async def raise_error():
    raise HTTPException(status_code=500, detail="This is the HTTP exception")

@app.get("/custom-error")
async def raise_custom_error():
    raise CustomException(status_code=500, message="This is the custom exception")