# Defining Request and Response Models

In your API, sometimes you may want to restrict what data is returned in the response. This is where response models come into play. Response models are used to define the structure of the response data that will be returned by your API. This is particularly useful when you want to return only a subset of the data that is available in the database or when you want to exclude certain fields from the response.

For example, when you have a `User` model with fields like `id`, `name`, `email`, and `password`, you may not want to return the `password` field in the response as it may be a security concern. Simiarly, usually the `id` field is auto generated and may not make sense to the client. So, you may also want to exclude `id` field in most cases. In such cases, you can define a response model that includes only the `name`, and `email` fields.

FastAPI uses Pydantic models to define response models. You can define a Pydantic model that includes only the fields you want to return in the response. Let's see how you can define a response model for the `Product` model.

```python
from pydantic import BaseModel, Field

products = []

class Product(BaseModel):
    id: int = Field(default=len(products) + 1, validate_default=True)
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(ge=0, description="Price must be greater than or equal to 0")
    brand: str = Field(min_length=3, max_length=50)
    category: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=50, max_length=150)

products.append(
    Product(
        id=1, 
        name="iPhone", 
        price=999.99, 
        brand="Apple", 
        category="Electronics", 
        description="A smart phone which is easy to use and intuitive from Apple (the leader in innovation)."
    )
)
products.append(
    Product(
        id=2, 
        name="Google Pixel 10", 
        price=599.99, 
        brand="Google", 
        category="Electronics", 
        description="A smart phone from leading search service provider. This company has access to lots of data points and helps you navigate your ways around the world. It's also one of the leaders in the AI space."
    )
)

class ProductResponse(BaseModel):
    name: str
    price: float
    brand: str
    description: str
```

This code is similar to previous tutorial code except that I have added couple of products to the `products` list. I have also defined a new Pydantic model `ProductResponse` that includes only the `name`, `price`, `brand`, and `description` fields. It doesn't include `id` and `category` fields from the `Product` model. This model will be used to define the response model for our products.

In the `main.py`, I have added type hint for the `get_item` function to use the `ProductResponse` model as the response model like below.

```python
async def get_item(product_id: int) -> ProductResponse:
    pass
```

Simiarly, the function `get_items` will return a list of `ProductResponse` models.

```python
from fastapi import FastAPI

from products import Product, products, ProductResponse

app = FastAPI()

@app.get("/products")
async def get_items() -> list[ProductResponse]:
    return products

@app.get("/products/{product_id}")
async def get_item(product_id: int) -> ProductResponse:
    for product in products:
        if product.id == product_id:
            return product

@app.post("/products")
async def add_product(product: Product):
    product.id = len(products) + 1
    products.append(product.dict())
    return product
```

And... that's all you need to do to define response models in FastAPI. You can now run the FastAPI application and test the endpoints using Swagger UI.

```bash
uvicorn main:app --reload
```

Open your browser and navigate to the `http://localhost:8000/products` and you will see two products in the response. Notice that the fields `id` and `category` are missing from these two products. Similarly, checkout `/products/1` endpoint to see `ProductResponse` as the response for that endpoint. 