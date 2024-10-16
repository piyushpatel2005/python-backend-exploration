---
title: "Args and Kwargs"
date: 2023-08-27T11:23:17-04:00
draft: false
---

Args and kwargs provide a way to pass multiple function arguments. This way we can make a general purpose function which can take variable number of arguments. 
<!--more-->
## Args

We can pass multiple values to a function and perform operations on those values using `*args`.

Let's say you want to define a `add` function that can take variable number of arguments and it will return the sum of all the values as its output. These kinds of functionality can be achieved using `*args` variables. 

This `args` variable holds the passed arguments in the form of a `tuple` as shown in the code below.

```python
def add(*args):
    print(args)
add(2,3) # (2, 3)
```

Once we have this tuple, we can extract individual elements by iterating through this tuple object.

**Example:**

```python
def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
    
print(add(2,3)) # 5
print(add(1,2,3)) # 6
print(add(1,2,3,4)) # 10
```

If we want to pass other arguments other than `args`, we can pass them before the `args` variable. If our function is accepting multiple parameters, then other named arguments should come before `args` variable. 

**Example:**

```python
def calculate(*args, department):
    sum = 0
    for num in args:
        sum += num

    print(f"Department {department}: {sum}")
```

**Output:**
```output{ lineNos=false }
TypeError: calculate() missing 1 required keyword-only argument: 'department
```

The `department` argument should come before `*args`. 
It's a common convention to name this variable argument variable as `args` in Python but we can name it whatever we wish.

```python
def calculate(department, *args):
    sum = 0
    for num in args:
        sum += num     
    print(f"Department {department}: {sum}")
    
calculate("Finance", 2, 3, 4) # Department Finance: 9
```

## Kwargs

`**kwargs` are similar concept to `*args` in that we can have parameters in the form of keyword arguments. These arguments will be available as a dictionary object with variable name as the keys.

```python
def sample_kwargs(**kwargs):
    print(kwargs)
sample_kwargs(name="Andrew", age=22) # {'name': 'Andrew', 'age': 22}
```

You can see that the arguments are passed as keyword arguments and they are available in dictionary named `kwargs`. It is common convention in Python community to name this variable as `kwargs`.

**Example:**

```python
def sample_kwargs(**kwargs):
    for key,value in kwargs.items():
        print("{0} : {1}".format(key, value)) 
sample_kwargs(name="Andrew", age=22)
```

**Output:**

```output{ lineNos=false }
name : Andrew
age : 22
```

## Additional Python Functions

There are few additional functions available in Python which can become quite useful.

- `abs()` function is used to find absolute value of a number. If the number is negative, this function returns the positive number for the same negative number. If the number was positive, it will not change anything.

```python
number = -10
print(abs(number)) # 10
number = -2.5
print(abs(number)) # 2.5
```

- `all()` functio ncan be used to check if all members of a collection data type are truthy or falsy values. In Python, some values are not exactly `False` but in conditional check, they behave like a `False`, so they are considered falsy values. These values include `None`, `False`, `0` as well as empty string.

```python
numbers = [1, 2, 3]
print(all(numbers)) # True
numbers = [0, 1, 2, 3]
print(all(numbers)) # False
items = [None, True, "hello"]
print(all(items)) # False
```

- Similarly, `any()` function can be used to check if any of the value is truthy.

```python
items = [0, "", False]
print(any(items)) # False
items = [0, "", True]
print(any(items)) # True
```

- `divmod()` function returns the quotient and remainder of the division operation as a tuple.

```python
quotient, remainder = divmod(5, 2)
print(quotient, remainder) # 2 1
```

- `isinstance()` method can be used to check if an object is an instance of specific class.

```python
name = "Victoria"
print(isinstance(name, str)) # True
```

- We can use `min()`, `max()` and `sum()` functions to find minimum, maximum and sum of all numbers from a list of numbers. If one of the element contains other data type, it will try to cast that value into numerical datatype. If it cannot be cast to number type, then it throws an error.

```python
numbers = [1, 2, 3]
print("Min:", min(numbers)) # Min: 1
print("Max:", max(numbers)) # Max: 3
print("Sum:", sum(numbers)) # Sum: 6
```