---
title: "Dictionaries"
date: 2023-08-27T11:22:48-04:00
draft: false
---

Dictionaries are also unordered container data type. It contains key-value pairs of data items. They are also called hashmap or associative arrays in other languages.
<!--more-->

## Creating Dictionary Objects

Dictionary can be created using curly braces (`{}`). We can also use `dict()` function to create a dictionary from collection of tuples. The keys and values are separated using colon (`:`) symbol.

```python
# Creating empty dictionary
empty_dict = {}
print(type(empty_dict)) # <class 'dict'>
```

We can create a dictionary with multiple key-value pairs. The key and the value should be separated using colon symbol (`:`).

**Example:**

```python
person = {"name": "Alex", "age": 25}
print(person) # {'name': 'Alex', 'age': 25}
```

A dictionary can have integer keys or a mixed data types for the keys.

```python
squares = {1: 1, 
           2: 4, 
           3: 9, 
           4: 16}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16}

example = {1: "one", "name": "Jacob"}
print(example) # {1: 'one', 'name': 'Jacob'}
```

In Python, we can pass a container datatype with tuples containing keys and values to `dict()` function and create a dictionary.

```python
person = dict([("name", "Alex"), ("age", 25)])
print(person) # {'name': 'Alex', 'age': 25}
```

## Accessing Data from a Dictionary

We can access specific values from dictionary using its key. In lists, we can access data using their indices, but in dictionary, the data is unordered and do not have indices. Dictionary values are accessed using its keys.

**Example:**

```python
person = dict((("name", "Alex"), ("age", 25)))
print(person["name"]) # Alex
print(person["age"]) # 25
```

If we try to access a key which doesn't exist, it will throw `KeyError`.

**Example:**

```python
person = {"name": "Alex", "age": 25}
print(person["city"])
```

**Output:**

```output{ lineNos=false }
KeyError: 'city'
```

To avoid this kind of errors, we can use the `get()` method to get an element from the dictionary. It takes the key as argument. Optionally, it also takes the default value to return if the key was not found.

**Example:**

```python
person = {"name": "Alex", "age": 25}
print(person.get("name")) # Alex
print(person.get("city")) # None
print(person.get("city", "Unknown")) # Unknown
```

We can add a new key-value pair or update the existing key-value pair easily by reassigning the key and values.

```python
person = {"name": "Alex", "age": 25}
# add key 'city' to person dictionary
person["city"] = "Toronto"
print(person) # {'name': 'Alex', 'age': 25, 'city': 'Toronto'}
# update the city for this person dictionary.
person["city"] = "New York"
print(person) # {'name': 'Alex', 'age': 25, 'city': 'New York'}
```

## Dictionary Methods

Dictionary objects are one of the most used data structures in Python. Python interpreter offers many built-in methods to easily work dictionary.

To remove a key-value pair, we can use `pop` method on the dictionary object.

```python
person = {"name": "Arjun", "age": 25, "country": "India"}
# Remove 'age' key-value pair
person.pop("age")
print(person) # {'name': 'Arjun', 'country': 'India'}
```

We could also remove any key-value pair using `del` operator.

```python
person = {"name": "Arjun", "age": 25, "country": "India"}
del person["age"]
print(person) # {'name': 'Arjun', 'country': 'India'}
```

With `del` operator, we can also completely remove the dictionary from system memory.

```python
person = {"name": "Alex", "age": 25, "country": "India"}
del person
print(person) # NameError: name 'person' is not defined
```

We can also use `len()` function on dictionary objects and get the number of keys in a given dictionary.

```python
person = {"name": "Alex", "age": 25, "country": "India"}
print(len(person)) # 3
```

We could get all keys or values in the form of a dictionary using `keys()` and `values()` methods on dictionary datatype. This returns iterable which we could easily cast them to `list` datatype by passing them as arguments to list() function. Although the ordering is not guaranteed so adding them to two separate lists may not be that useful.

```python
person = {"name": "Alex", "age": 25, "country": "India"}
print(list(person.keys())) # ['name', 'age', 'country']
print(list(person.values())) # ['Alex', 25, 'India']
```

We could also set a default value for specific key in the dictionary. If the dictionary object already contains that key, it will return the value corresponding to that, but if that key doesn't exist, when we look up for that key, it returns the default value.

**Example:**

```python
person = {"name": "Alex", "age": 25, "country": "India"}
person.setdefault("country", "confidential")
print(person["country"]) # India

person = {"name": "Alex", "age": 25}
person.setdefault("country", "confidential")
print(person["country"]) # confidential
```

We could create a copy of a dictionary using `copy()` method. If we try to directly assign the variable to another variable name, Python interpreter will not actually create a copy. It will only point the new variable to the same memory location as the older dictionary object. This is also called shallow copy. This can be verified by checking the id of each object using `id()` function.

```python
person = {"name": "Alex", "age": 25}
person2 = person
print(id(person), id(person2)) # 1831689209024 1831689209024

person3 = person.copy()
print(id(person), id(person2)) # # 1831689209024 1831689241216
```

We can also clear all key-value pairs from dictionary using `clear()` method.

```python
person = {"name": "Alex", "age": 25, "country": "Canada"}
print(person) # {'name': 'Alex', 'age': 25, 'country': 'Canada'}
person.clear()
print(person) # {}
```

## Iterating through Dictionary

Dictionary objects contain key-value pairs and do not have any index, so we cannot iterate through them simply like lists or tuples. They are unordered collection of key-value pairs. But if we recall `items()` method, we get list of key-value tuples. This helps us iterate through all items of the dictionary.

**Example:**

```python
person = {"name": "Alex", "age": 25, "country": "Canada"}
for item in person.items():
    print(item)
```

**Output:**

```output{ lineNos=false }
('name', 'Alex')
('age', 25)
('country', 'Canada')
```

We can unpack those pairs of key-value using the tuple unpacking and get keys and values.

**Example:**

```python
person = {"name": "Alex", "age": 25, "country": "Canada"}
for key,value in person.items():
    print(f"{key} : {value}")
```

**Output:**

```output{ lineNos=false }
name : Alex
age : 25
country : Canada
```

We can also iterate over only keys using `keys()` method.

**Example:**

```python
person = {"name": "Alex", "age": 25, "country": "Canada"}

for key in person.keys():
    print(key)
```

**Output:**

```output{ lineNos=false }
name
age
country
```

For values, we can use `values()` method.

**Example:**

```python
person = {"name": "Alex", "age": 25, "country": "Canada"}

for value in person.values():
    print(value)
```

**Output:**

```output{ lineNos=false }
Alex
25
Canada
```

## Dictionary Comprehension

Dictionary comprehension is similar to list comprehension but in this case, we will be creating dictionary instead of lists.

The general syntax looks like this

```python
{expression for elem in dictionary}
```

If we want to convert below `numbers` dictionary into its respective `squares` dictionary, we can do that using dictionary comprehension.

**Example:**

```python
numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
squares = {key: value * value for key, value in numbers.items()}
print(squares) # {'one': 1, 'two': 4, 'three': 9, 'four': 16}
```

To swap keys with values from a dictionary, we can use below.

**Example:**

```python
numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
swapped = {value: key for key, value in numbers.items()}
print(swapped) # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
```

We can also apply conditions using `if` clause to add only certain key-value pairs.

```python
numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
even_numbers = {key: value for key, value in numbers.items() if value % 2 == 0}
print(even_numbers) # {'two': 2, 'four': 4}
```

We could also apply multiple conditions using multiple `if` clauses. We don't need to have `and` operator between each `if` clause. It works as if it has `and` between each conditioanls.

```python
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8}
higher_evens = {key: value for key, value in numbers.items() if value > 4 if value % 2 == 0}
print(higher_evens) # {'six': 6, 'eight': 8}
```