# Tuples in Python

Tuples are immutable collection data structure in Python. They are very similar to lists except that we cannot modify the elements of a tuple, they are immutable.

## Creating Tuples

We can create tuple using pair of parenthesis `()` or by using built-in function `tuple()`. The `tuple` function takes an iterable and converts that into a tuple of elements.

**Example:**

```python
()
tuple()
(1, 2, 3)
tuple(range(2))
tuple([1, 2, 3])
```

Tuples are an object of `tuple` class. We can check the type using `type()` function.

**Example:**

```python
numbers = (1, 2, 3)
print(numbers) # (1, 2, 3)
print(type(numbers)) # <class 'tuple'>
```

Tuples can also be of mixed data types. They can include numbers, strings or booleans in the same tuple.

```python
mixed_tuple = (1, 'Bob', True)
```

Tuples can also be nested just like Python lists. 

```python
nested_tuple = (1, True, ("orange", "banana"))
```

If we want to create a tuple of single element, we have to append comma at the end of element to denote that this is list. If we don't write comma, Python interpreter will create a string object.

```python
fruits = ('apple')
print(type(fruits)) # str

another_fruits = ('apple',)
print(type(another_fruits)) # tuple
```

**Output:**

```output{ lineNos=false}
<class 'str'>
<class 'tuple'>
```

One more interesting fact about tuples is that while creating a tuple, we don't explicitly have to wrap them in parentheses. Python will take list of comman separated elements and mark them as tuples.

```python
fruits = 'apple', 'orange', 'mango'
print(type(fruits)) # <class 'tuple'>
```

## Indexing

Tuple indexing works similar to lists. They are zero-indexed.

```python
numbers = (1, 2, 3, 4, 5)
print(numbers[0]) # 1
print(numbers[-1]) # 5

nested_tuple = (1, True, ("orange", "banana"), 23)
print(nested_tuple[2]) # ('orange', 'banana')
print(nested_tuple[2][0]) # 'orange'
```

We can get the length of a tuple using `len()` function.

```python
numbers = (1, 2, 3, 4, 5)
print(len(numbers)) # 5
```

Tuples are immutable. So, if we try to modify an element of a tuple, Python interpreter throws a `TypeError`.

```python
numbers = (1, 2, 3, 4, 5)
numbers[4] = 500
```

```output{ lineNos=false }
TypeError: 'tuple' object does not support item assignment
```

## Slicing

We can perform slicing operations like Python lists. Tuple slicing operation will return a new tuple with slice of elements from the original tuple.
Again, the syntax for slicing looks like `tuple[start:stop:step]`. We can omit any of these three parts in slicing `start`, `stop` or `step`.

```python
fruits = ('apple', 'banana', 'mango', 'orange', 'pineapple')
print(fruits[2:4]) # ('mango', 'orange')
print(fruits[2:]) # ('mango', 'orange', 'pineapple')
print(fruits[:3]) # ('apple', 'banana', 'mango')
print(fruits[::-1])
```

Elements can be reversed by specifying negative value for `step`.

```python
print(fruits[::-1]) # ('pineapple', 'orange', 'mango', 'banana', 'apple')
```

## Looping through Tuple Elements

Tuples are iterables like lists. So, we can iterate through elements of a tuple using simple `for` loops in Python.

**Example:**

```python
fruits = ('apple', 'banana', 'orange')
for fruit in fruits:
    print(fruit)
```

**Output:**

```output{ lineNos=false }
apple
banana
orange
```

If we want to also use index position of each element, we can use `enumerate` function which give tuple of each index and element.

**Example:**

```python
colors = ("white", "red", "blue", "brown")
for index, color in enumerate(colors):
    print(index, color)
```

**Output:**

```output{ lineNos=false }
0 white
1 red
2 blue
3 brown
```

## Unpacking Tuples

We can unpack a tuple into multiple elements. This provides elegant syntax for variable assignment. In this make sure that the number of elements of a tuple on the right hand side matches the number of variables we want to assign on the left hand side.

**Example:**

```python
tup = (1, 2, "John")
a, b, c = tup
print(a, b, c) # 1 2 John
```

This method is also very useful when we want to return multiple values from a Python function. For example, below function returns sum and product of two numbers in the form of tuple.

**Example:**

```python
def sum_product(num1, num2):
    return num1 + num2, num1 * num2

sum, product = sum_product(2,4)
print("Sum of 2 and 4 is {sum}".format(sum=sum))
print("Product of 2 and 4 is {product}".format(product=product))
```

**Output:**

```output{ lineNos=false }
Sum of 2 and 4 is 6
Product of 2 and 4 is 8
```

This also provides neat trick to swap two numbers.

```python
num1 = 1
num2 = 2
print(num1, num2) # 1 2
# Swap numbers
num1, num2 = num2, num1
print(num1, num2) # 2 1
```

## Tuple Functions

There are few useful functions with tuple data structure.
We can join two tuples using `+` operator and it will return elements of both tuples.

```python
numbers = (1, 2, 3)
others = (4, 5, 6)
numbers + others # (1, 2, 3, 4, 5, 6)
```

We can have elements of a tuple repeated specific number of times in a new tuple.

```python
numbers = (1, 2)
numbers * 3 # (1, 2, 1, 2, 1, 2)
```

To find index position of a specific element in a tuple, we can use `index()` method. If the element exists, Python interpreter will return the index of that element. If the element does not exist, we get `ValueError`.

```python
fruits = "apple", "orange", "banana"
fruits.index("banana") # 2
fruits.index("peach") # ValueError: tuple.index(x): x not in tuple
```

We can use `in` operator to find if an element exists in a tuple. This returns boolean result `True` if element exists else `False`.

**Example:**

```python
numbers = tuple(range(1, 11, 2))
print(numbers) # (1, 3, 5, 7, 9)
print(3 in numbers) # True
print(4 in numbers) # False

fruits = ("apple", "banana", "grapes")
"grapes" in fruits # True
```

We can find how many times a specific element occurs in a tuple using `count()` method.

```python
numbers = (1, 2, 3, 7, 4, 3)
print(numbers.count(3)) # 2
```

We can delete complete tuple using `del` operator. 

```python
numbers = (1, 2, 3)
del numbers # remove the tuple from memory
```