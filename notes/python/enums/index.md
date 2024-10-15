# Python Enums

In Python, an enumeration is a set of symbolic names (members) bound to unique, constant values. Enums are created using the `enum` module. Enums are useful when you have a fixed set of values that are related to each other. Enums provide a way to define a set of named constants that are more readable and maintainable than using plain strings or integers.

## Overview

Enums are great when you have a predefined set of values that are related to each other. For example, let's say you're an online platform providing different kinds of payment methods. You could define those payments methods in an enum. Similarly, the order status could be defined in an enum.

### Benefits of Enums

- Enums provide a way to define a set of named constants that are more readable and maintainable than using plain strings or integers.
- Enums can be iterated over, compared, and used in `if` statements.
- Enums can be used to define a fixed set of values that are related to each other.
- Enums reduce the chances of errors due to typos or incorrect values because they can have only set of defined values. For example, if the `OrderStatus` was defined as a string, a developer could type `PENDING` as `PENDINGG` by mistake, which would be hard to catch. With enums, this is very easily avoided.
- Enums provide kind of type safety. If you have a function that expects an `OrderStatus`, you can be sure that the value passed to the function is a valid `OrderStatus`.

## Defining Enums

Enums are defined using the `Enum` class from the `enum` module. Enums can be created using the `class` syntax. Enums can be iterated over, compared, and used in `if` statements.

```python
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

# Accessing enum members
print(OrderStatus.PENDING) # OrderStatus.PENDING
print(OrderStatus.PROCESSING.name) # PROCESSING
print(OrderStatus.SHIPPED.value) # 3
print(OrderStatus.DELIVERED == OrderStatus.DELIVERED) # True
print(type(OrderStatus.SHIPPED)) # <enum 'OrderStatus'>
print(OrderStatus.SHIPPED == 3) # False
```


In above code, I've defined an enum `OrderStatus` which extends `Enum` class. The members of the enum are defined as class attributes. Each member has a name and a value. The name is the string used to access the member, and the value is the value of the member. 

The cool thing with enums is that you can access the members using the dot notation. You can also access the name and value of the members. You can compare the members using `==` operator. You can also check the type of the member. Interestingly, even though the value of `OrderStatus.SHIPPED` is `3`, it's not equal to `3` because they are of different types. So, this will avoid mistakes where you might accidentally compare an enum member with an integer.

### Iterating Over Enums

Enums can be iterated over using a `for` loop. When you iterate over an enum, you get the members of the enum.

```python
from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

for status in OrderStatus:
    print(status)
```

## Enums with String Values

You can also define enums with string values.

```python
from enum import Enum

class PaymentMethod(Enum):
    CASH = 'cash'
    CARD = 'card'
    TRANSFER = 'transfer'

print(PaymentMethod.CASH) # PaymentMethod.CASH
print(PaymentMethod.CARD.value) # card
```

In this example, I've defined an enum `PaymentMethod` with string values. The members of the enum are defined as class attributes. Each member has a name and a value. The name is the string used to access the member, and the value is the value of the member.

The `enum` module also provides specific types of enums like `IntEnum` and `StrEnum` which can be used to define enums with integer and string values respectively.

```python
from enum import StrEnum

class OrderStatus(StrEnum):
    PENDING = 'pending',
    PROCESSING = 'processing',  
    SHIPPED = 'shipped',
    DELIVERED = 'delivered',
    CANCELLED = 'cancelled'

for status in OrderStatus:
    print(status)
```

Similarly, you can use `IntEnum` to define enums with integer values which is straight forward based on above example.

## Enums with `auto()` function

The `enum` module also provides `auto()` function which can be used to automatically assign values to the members of the enum. This is quite handly as it provides a way to avoid assigning values manually. It will create values based on number of members in the enum. By default these numbers start with `1`. 

```python
from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = auto(),
    PROCESSING = auto(),
    SHIPPED = auto(),
    DELIVERED = auto(),
    CANCELLED = auto()

print(OrderStatus.PENDING.value) # 1
```

### Generating Custom Values

By default these values are generated based on the method `_generate_next_value_()` which is defined in the `Enum` class. You can override this method to provide custom values for enums.

```python
from enum import Enum, auto

class OrderStatus(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    PENDING = auto(),
    PROCESSING = auto(),
    SHIPPED = auto(),
    DELIVERED = auto(),
    CANCELLED = auto()

print(OrderStatus.PENDING.value) # pending
```

In this tutorial, you learned about how to use enums in your code to make it more maintainable. It also covered multiple ways to define enums and how to use them in your code.
