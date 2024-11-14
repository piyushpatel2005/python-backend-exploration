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
    Product(id=1, name="iPhone", price=999.99, brand="Apple", category="Electronics", description="A smart phone which is easy to use and intuitive from Apple (the leader in innovation).")
)
products.append(
    Product(id=2,
            name="Google Pixel 10",
            price=599.99,
            brand="Google",
            category="Electronics",
            description="A smart phone from one of the leaders in the AI space. These devices can easily help you navigate the world."
            )
)

class ProductResponse(BaseModel):
    name: str
    price: float
    brand: str
    description: str