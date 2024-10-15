# Pydantic Overview

In programming, often we need to keep related variables and methods together in a single unit. This is where classes come in. Classes are a way to bundle data and methods together. In Python, classes are defined using the `class` keyword. We could use collectiosn like tuples, dictionaries, or lists to store data, but classes provide a way to organize data and methods in a more structured way.

```python
class Cat: 
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def meow(self):
        return f"{self.name} says meow"

cat = Cat("Fluffy", 3)
```

## Data classes

Python also has a concept of data classes. Data classes are classes that are primarily used to store data. They are similar to regular classes, but they come with some additional features. Data classes are defined using the `@dataclass` decorator from the `dataclasses` module. Data classes are a way to reduce boilerplate code when defining classes that are primarily used to store data. In this case, we don't need to define the `__init__` method, and we don't need to define the attributes explicitly. So, it's lot more succinct.

```python
from dataclases import dataclass

@dataclass
class Cat:
    name: str
    age: int

cat = Cat("Fluffy", 3)
```

These are simple solutions but they lack the data validations. You could definitely implement your own solution to validate the data, but it would be a lot of boilerplate code. This is where Pydantic comes in. 

### Features of Pydantic
Pydantic is a data validation library that provides data validation and parsing using Python type annotations. Pydantic is a great library for data validation and parsing in Python. It is particularly useful when working with APIs and web applications where data validation is crucial. FastAPI integrates well with Pydantic and uses Pydantic models to validate request data and serialize response data. Below are some of the featuers of Pydantic.

- Type hints: Pydantic uses Python type hints to define the structure of the data.
- Data validation: Pydantic validates the data based on the type hints by default. It also provides additional validation features like min, max, regex, etc.
- Data parsing: Pydantic can parse the data from different sources like JSON, form data, query parameters, etc.
- Serialization: Pydantic can serialize the data to different formats like JSON, XML, etc.
- Custom validation: Pydantic allows you to define custom validation logic using methods.
- Speed: Pydantic is fast and efficient. It uses a compiled model to validate and parse the data.

Let's see few examples of how to use Pydantic models.

## Pydantic BaseModel

Pydantic provides a `BaseModel` class that we can use to define Pydantic models. Pydantic models are used to define the structure of the data that we expect to receive in the request or send in the response. Pydantic models are defined using Python type hints. They can be used to validate the data, parse the data, and serialize the data into JSON or other formats. 

Let's say I have defined my `Order` model using Pydantic `BaseModel` in `models.py` module.

```python
from datetime import date
from enum import StrEnum, auto
from pydantic import BaseModel

class OrderStatus(StrEnum):
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    COMPLETED = auto()

class Order(BaseModel):
    order_id: int
    order_date: date
    status: OrderStatus = OrderStatus.PENDING
    amount: float
```

Now, to create an `Order` I can create it like this.

```python
from models import Order
from datetime import date

order = Order(order_id=1, order_date=date(2024, 9, 30),  amount=100.0)
print(order)
```

This works very well as long as we have the correct data types passed to the `Order` constructor. If you pass a string to `order_id` or a date in the ISO string format, Pydantic will raise a validation error. Pydantic will also raise an error if you pass an invalid value to the `status` field. In this case, the last error is less likely because I'm using an `Enum` to define the `OrderStatus` field, but let's see what happens if other fields have invalid values.

```python
order = Order(order_id="1", order_date="30 September 2024", amount=100.0)
print(order)
```

This will raise a `ValidationError` with the following message.

```output { lineNos=false }
pydantic_core._pydantic_core.ValidationError: 1 validation error for Order
order_date
  Input should be a valid date or datetime, invalid character in year [type=date_from_datetime_parsing, input_value='30 September 2024', input_type=str]
```

This is great because you don't have to check for these validations manually. Pydantic will do it for you. Pydantic also provides lots of other validators that you can use to validate the data. You can use validators like `min_length`, `max_length`, `regex`, etc. You can also define custom validators using methods.

## Working with JSON

You can serialize and deserialize JSON objects easily with Pydantic

### Creating Python objects from JSON

Pydantic can also parse the data from JSON and create objects from it. This is very useful when working with APIs where the data is sent in JSON format. Pydantic can parse the JSON data and create objects from it. This can be handy when you're working with web APIs. You can easily create new objects using `model_validate_json()` method by passing json string for the object. Let's see an example of how to create an `Order` object from JSON data.

```python
from models import Order

order_data = """
{
    "order_id": 1,
    "order_date": "2024-09-30",
    "amount": 100.0
}
"""

order = Order.model_validate_json(order_data)
print(order)
```

This will create an `Order` object from the JSON data. Pydantic will parse the JSON data and create an `Order` object from it. If the JSON data is invalid, Pydantic will raise a `ValidationError`.

### Converting Python object to JSON

You can also convert the Python object to JSON using the `json()` method. This will serialize the object into a JSON string.

```python
order = Order(order_id=1, order_date=date(2024, 5, 8),  amount=100.0)
order_json = order.model_dump_json()
print(order_json)
```

**Output:**

```output { lineNos=false }
{"order_id":1,"order_date":"2024-09-30","status":"pending","amount":100.0}
```

## Creating Objects from Dict

You could also create an object from a dictionary. This is useful when you're working with APIs where the data is sent as a dictionary. You can easily create new objects using `model_validate()` method by passing a dictionary for the object. Let's see an example of how to create an `Order` object from a dictionary.

```python
from models import Order

order_data = {
    "order_id": 1,
    "order_date": "2024-09-30",
    "amount": 100.0
}

order = Order.model_validate(order_data)
print(order)
```

Again, just like JSON, you can convert Python objects to a dictionary using the `model_dump()` method.

```python
order = Order(order_id=1, order_date=date(2024, 6, 1),  amount=100.0)
order_json = order.model_dump()
print(order_json)
```