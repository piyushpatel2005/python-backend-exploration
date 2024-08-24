# Query Parameters in FastAPI

Query parameters are used to pass data to the server as key-value pairs in the URL. They are appended to the URL after a question mark `?` and separated by an ampersand `&`. Query parameters are used to filter, sort, and paginate data in the API. The url with query parameters looks like this:

```
https://example.com/items?sort=price&order=asc&page=1
```

FastAPI can automatically parse query parameters from the URL and pass them to the route handler function. Query parameters are defined as arguments to the route handler function with default values. FastAPI will automatically convert the query parameters to the specified data type.
Let's take an example of this below.

## Query Parameters Example

Below app looks very similar to the one we had for previous lesson. The only change is in `get_items` function where we have added query parameters `sort` and `order`. These query parameters are used to sort the items by `sort` field and order them in ascending or descending order based on the `order` parameter.

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


@app.get("/")
async def home():
    return {"message": "Welcome to our Ecommerce API!"}


@app.get("/products")
async def get_items(sort: str = None, order: str = None):
    if sort is None:
        return products
    else:
        if order == "asc":
            return sorted(products, key=lambda x: x[sort])
        elif order == "desc":
            return sorted(products, key=lambda x: x[sort], reverse=True)
        else:
            return {"error": "Invalid order parameter. Use 'asc' or 'desc'."}


@app.get("/products/{product_id}")
async def get_item(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
```

If you have a function declared with more parameters than what the route handles, FastAPI will automatically assume the extra parameters as query parameters. In the above example, `sort` and `order` are query parameters. If you call the `/products` endpoint without any query parameters, it will return all the products. If you call the `/products` endpoint with `sort` and `order` query parameters, it will sort the products based on the `sort` field and order them in ascending or descending order based on the `order` parameter.

Try below URLs in your browser to see the results sorted by price in descending order.

```bash
http://localhost:8000/products?sort=price&order=desc
```

Now, change the `order` parameter to `asc` to see the results sorted by price in ascending order.

```bash
http://localhost:8000/products?sort=price&order=asc
```

You could also change the `sort` parameter to `id` to see the results sorted by id in ascending order.

```bash
http://localhost:8000/products?sort=id&order=asc
```

This can be very useful when you want to filter, sort, and paginate data in your API. FastAPI makes it very easy to work with query parameters in your API.

## Order of Query Parameters

The order of query parameters in the URL does not matter. FastAPI will automatically parse the query parameters and pass them to the route handler function in the order they are defined. You can change the order of query parameters in the URL and it will still work as expected.

The same is true when we also have path parameters in the URL. FastAPI will automatically parse the path parameters and query parameters and pass them to the route handler function in the order they are defined in the function.

```bash
http://localhost:8000/users/1/connections?sort=name&order=asc
```

In the above URL, `1` is the path parameter and `sort` and `order` are query parameters. 

The definition of handler for this might look like this. This endpoint can be used to find the connections of a user and sort them by name in ascending order.

```python
@app.get("/users/{user_id}/connections")
async def get_user_connections(user_id: int, sort: str = None, order: str = None):
    # Your code here
    pass
```

In this case, `user_id` is a path parameter and `sort` and `order` are query parameters. FastAPI will automatically parse the path parameter `user_id` and query parameters `sort` and `order` and pass them to the route handler based on the order they are defined in the function.