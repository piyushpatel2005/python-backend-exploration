---
title: Path Parameters
sidebar:
  order: 6
---

In HTTP, the path is the part of the URL that comes after the domain name. This path can either be fixed or variable. For example, in the URL `https://example.com/users/123`, the path is `/users/123`. Here, `123` is a variable part of the path that represents the user ID. The fixed path is `/users/`, and can refer to a list of users. In this cae, we may want to retrieve a specific user by their ID. Similarly, if the url  is `https://example.com/users/125`, the path is `/users/125`. The intent of this url is to retrieve the user with ID `125`. This `id` will likely be change with every request and we need a way to capture this value from the URL path.

## How to use Path Parameters in FastAPI

Path parameters are used to capture values from the URL path. FastAPI can identify these variable parameters in the path and pass them to the route handler function. Path parameters are defined by including a variable name in the path string enclosed in curly braces `{}`. The variable name is then used as an argument in the route handler function.

Now, when we create `FastAPI` application object, that object acts as a router. We can define routes using the `@app.get`, `@app.post`, `@app.put`, `@app.delete` decorators. The `@app.get` decorator is used to define a route that responds to HTTP GET requests. The route we define is `/`, which is the root URL of the application. This can be accessed at the URL `http://localhost:8000/` when we run the server locally. So, basically `@app.get` decorator is used to map a Python function to specific route.

## Example API with Path Parameters

```python
from fastapi import FastAPI

app = FastAPI()


products = [
    {"id": 1, "name": "iPhone", "price": 999.99, "brand": "Apple", "category": "Phones", "description": "The iPhone is a smartphone made by Apple Inc."},
    {"id": 2, "name": "Galaxy", "price": 899.99, "brand": "Samsung", "category": "Phones", "description": "The Galaxy is a smartphone made by Samsung."},
    {"id": 3, "name": "Pixel", "price": 799.49, "brand": "Google", "category": "Phones", "description": "The Pixel is a smartphone made by Google."},
    {"id": 4, "name": "Dell XPS", "price": 999.99, "brand": "Dell", "category": "Laptops", "description": "The Dell XPS is a laptop made by Dell Inc."},
    {"id": 5, "name": "MacBook Pro", "price": 1999.99, "brand": "Apple", "category": "Laptops", "description": "The MacBook Pro is a laptop made by Apple Inc."},
    {"id": 6, "name": "ThinkPad", "price": 999.99, "brand": "Lenovo", "category": "Laptops", "description": "The ThinkPad is a laptop made by Lenovo."},
    {"id": 7, "name": "iPad", "price": 799.99, "brand": "Apple", "category": "Tablets", "description": "The iPad is a tablet made by Apple Inc."},
    {"id": 8, "name": "Galaxy Tab", "price": 699.99, "brand": "Samsung", "category": "Tablets", "description": "The Galaxy Tab is a tablet made by Samsung."},
    {"id": 9, "name": "Fire HD", "price": 499.99, "brand": "Amazon", "category": "Tablets", "description": "The Fire HD is a tablet made by Amazon."},
    {"id": 10, "name": "Apple Watch", "price": 399.99, "brand": "Apple", "category": "Wearables", "description": "The Apple Watch is a wearable made by Apple Inc."},
    {"id": 11, "name": "Galaxy Watch", "price": 299.99, "brand": "Samsung", "category": "Wearables", "description": "The Galaxy Watch is a wearable made by Samsung."},
    {"id": 12, "name": "Fitbit", "price": 199.99, "brand": "Fitbit", "category": "Wearables", "description": "The Fitbit is a wearable made by Fitbit Inc."},
    {"id": 13, "name": "Motorola Razr", "price": 1499.99, "brand": "Motorola", "category": "Phones", "description": "The Motorola Razr is a smartphone made by Motorola Inc."},
    {"id": 14, "name": "OnePlus", "price": 699.99, "brand": "OnePlus", "category": "Phones", "description": "The OnePlus is a smartphone made by OnePlus Inc."}
]


@app.get("/products")
async def get_items():
    return products


@app.get("/produts/{product_id}")
async def get_item(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
```

In above code, I have defined `products` as list of products I've available in my store. I have included three routes for this web API.

1. `/`: This is the root URL of the application. When we access this URL, it will return a JSON response with a message `Hello, World`.
2. `/items`: This route will return all the items available in the store.
3. `/items/{item_id}`: This route will return the item with the specified `item_id`. The `item_id` is a path parameter that is captured from the URL path. The `item_id` is passed as an argument to the `get_item` function which is route handler for this path.

When you run the server and access the URL `http://localhost:8000/items/1`, the `get_item` function will be called with `id=1`. The function will iterate over the `items` list and return the item with `id=1`.

```bash
uvicorn main:app --reload
```

Try paths with different `item_id` values to see the different items returned by the API. For example, `http://localhost:8000/items/1` will return the following JSON response.

```json
{"id": 1, "name": "iPhone", "price": 999.99, "brand": "Apple", "category": "Phones", "description": "The iPhone is a smartphone made by Apple Inc."}
```

Interestingly, when we return `items` from the `get_item` function, we are actually returning Python dictionary and not JSON object. FastAPI automatically converts the Python dictionary to JSON format. This is because FastAPI uses Pydantic models to serialize and deserialize data. Pydantic is a data validation and parsing library for Python. It defines a schema for the data and validates the data against the schema.

## Order Matters

In above example, we had only two endpoints, however, if I add another endpoint like this in the middle of the two endpoints above.

```python
@app.get("/products")
async def get_items():
    return items


@app.get("/produts/{product_id}")
async def get_item(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

@app.get("/products/all")
async def get all_items():
    return items
```

In this case, when I try to access `/products/all` endpoint, I get `404 Not Found` error because the FastAPI cannot parse  `all` as an integer and it tries to match the path parameter with the second endpoint which is `/products/{product_id}`. To fix this, we need to move the `/products/all` endpoint above the `/products/{product_id}` endpoint. 

```python
@app.get("/products/all")
async def get all_items():
    return items

@app.get("/produts/{product_id}")
async def get_item(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
```

So, the order of endpoints matter if two endpoints match the same path but with different path parameters.

Overall, It's so easy to write RESTful APIs with FastAPI. We can define routes and path parameters with just a few lines of code. FastAPI takes care of the rest, including data validation, serialization, and deserialization.
