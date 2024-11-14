# Error Handling in FastAPI

Error handling is critical in any production application. FastAPI provides built-in exception handlers to handle errors gracefully. In this tutorial, you will learn how to handle errors in FastAPI.

## Handling Errors

When an error occurs in your FastAPI application, it will return a JSON response with the error details. The response will include the error message and the status code. FastAPI provides a default exception handler that returns the error message and status code. By default, when you don't have any custom exception handling code, FastAPI will return a JSON response with the error message and status code.

Below is an example of a FastAPI application that raises an exception.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/error")
async def raise_error():
    raise HTTPException(500, "This is an exception")
```

Now, when you run the FastAPI application and navigate to the `/error` endpoint, it will raise an exception and the server will return `500 Internal Server Error` status code with below json response. 

```json
{
    "detail": "This is an exception"
}
```

## Custom Exception Handlers

You can also define custom exception handlers to handle specific errors.

Below code defines a custom exception handler for `HTTPException` that returns a custom error message and status code.

```python
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "There was a server error"},
    )

@app.get("/error")
async def raise_error():
    raise HTTPException(status_code=500, detail="This is the HTTP exception")
```

In this case, you have imported `HTTPException` and `JSONResponse` from FastAPI and Starlette respectively. You have defined a custom exception handler `http_exception_handler` that returns a JSON response with the error message and status code. The function is decorated with `@app.exception_handler()` which specifies what kind of exception it handles. The `status_code` is set to the status code of the exception and the `content` is set to a custom error message. Often it's better to hide the actual error message from the user for security reasons. So, this code returns a generic error message.

This time when you run the FastAPI application and navigate to the `/error` endpoint, it will raise an exception and the server will return `500 Internal Server Error` status code with below json response. 

```json
{
    "message": "There was a server error"
}
```

You can also define multiple custom exception handlers for different types of exceptions. Below code adds two different exception handlers based on the type of the exception.

```python
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
```
