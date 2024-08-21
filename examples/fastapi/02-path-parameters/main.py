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
def home():
    return {"message": "Hello, World"}


@app.get("/products")
def get_items():
    return products


@app.get("/products/{product_id}")
def get_item(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
