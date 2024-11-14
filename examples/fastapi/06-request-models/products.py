from pydantic import BaseModel, Field
from typing import Optional

products = []

# class Product(BaseModel):
#     id: Optional[int] = None
#     name: str
#     price: float
#     brand: str
#     category: str
#     description: str

class Product(BaseModel):
    id: int = Field(default=len(products) + 1, validate_default=True)
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(ge=0, description="Price must be greater than or equal to 0")
    brand: str = Field(min_length=3, max_length=50)
    category: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=50, max_length=150)