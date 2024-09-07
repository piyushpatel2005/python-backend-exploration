from fastapi import FastAPI, Body

app = FastAPI()

products = [
    {"id": 1, "name": "iPhone", "price": 999.99, "brand": "Apple", "category": "Phones",
     "description": "The iPhone is a smartphone made by Apple Inc."},
    {"id": 2, "name": "Galaxy", "price": 899.99, "brand": "Samsung", "category": "Phones",
     "description": "The Galaxy is a smartphone made by Samsung."},
    {"id": 3, "name": "Pixel", "price": 799.49, "brand": "Google", "category": "Phones",
     "description": "The Pixel is a smartphone git smade by Google."}
]


@app.get("/products")
async def get_items():
    return products


@app.get("/products/{product_id}")
async def get_item(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product


@app.post("/products")
async def add_product(name: str = Body(), price: float = Body(), brand: str = Body(), category: str = Body(),
                      description: str = Body()):
    product = {"id": len(products) + 1, "name": name, "price": price, "brand": brand, "category": category,
               "description": description}
    products.append(product)
    return product


@app.put("/products/{product_id}")
async def update_product(product_id: int, name: str = Body(), price: float = Body(), brand: str = Body(),
                            category: str = Body(), description: str = Body()):
        for product in products:
            if product["id"] == product_id:
                product["name"] = name
                product["price"] = price
                product["brand"] = brand
                product["category"] = category
                product["description"] = description
                return product


@app.patch("/products/{product_id}")
async def update_product(product_id: int, name: str = Body(None), price: float = Body(None), brand: str = Body(None),
                            category: str = Body(None), description: str = Body(None)):
        for product in products:
            if product["id"] == product_id:
                product["name"] = name if name else product["name"]
                product["price"] = price if price else product["price"]
                product["brand"] = brand if brand else product["brand"]
                product["category"] = category if category else product["category"]
                product["description"] = description if description else product["description"]
                return product


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return product
    return {"message": "Product not found"}