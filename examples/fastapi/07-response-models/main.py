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