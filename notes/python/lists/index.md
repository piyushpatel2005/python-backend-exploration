# Python Lists

Lists are collection of different elements of different data types although usually they will be of the same data type. It is a container that can hold primitive data types as well as user-created data types. This lessons show how to create and use lists.

- List is a sequence of elements.
- Lists are mutable data structure. We can modify elements of the list using indexing operation.
- Lists are iterable so we can iterate through each item of the list.

## Creating Lists in Python

There are couple of ways to create a list. 
1. Using square brackets `[]`.
2. Using built-in function `list`.

**Example:**

```python
numbers = [1, 2, 3, 4, 5]
print(numbers)
```

In above example, we created a list with elements 1 to 5.

**Output:**
```output{ lineNos=false }
[1, 2, 3, 4, 5]
```

We can create empty list using below syntax. Alternatively, we can use `list()` function as shown below. This function takes in any iterable and returns a list of those elements.

```python
empty_list = []
another_empty_list = list()
```

We can create lists of numbers or string data types or any other data type if we want.

```python
numbers = [1, 2, 3]
fruits = ['apple', 'orange', 'banana']
```

List can also contain multiple data types.

**Example:**

```python
mixed_list = [1, 2, True, "banana", False]
```

We can also create nested lists. These are also called multi-dimensional lists.

```python
nested_list = [[1, 2], [3, 4]]
```

We can also pass a `range` object into `list` function to create a list.

**Example:**

```python
numbers = list(range(5))
print(numbers)
```

**Output:**

```outpu{ lineNos=false }
[0, 1, 2, 3, 4]
```

Just like strings, we can use same range function with start, stop and step values to create a list.

```python
even_numbers = list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
```

We can create list from any iterable using `list()` function.

```python
list("Hello") # ['H', 'e', 'l', 'l', 'o']
```

## List Indexing

Lists are indexed using 0-based indexing. That is the first element of the list is at index position `0` just like strings. We can also use negative indices, i.e. the last element of the list can be accessed easily using `-1` index.

**Example:**

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[3]) # 4
print(numbers[-1]) # 5
```

Lists are mutable so we can modify each element of the list using their index.

**Example:**

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[3]) # 4
numbers[3] = 400
print(numbers[3]) # 400
```

If we try to access an element at index position, which doesn't exist in the list, Python interpreter will throw `IndexError`.

**Example:**

```python
print(numbers[5]) # IndexError: list index out of range
```

To find how many elements are there in a list, we can use built-in `len()` function. We can also use this function to access the last element and to avoid `IndexError` for accessing elements.

```python
print(len(numbers)) # 5

# To access last element of the list, use len() function
print(numbers[len(numbers) - 1]) # 5

# or even better use negative index
print(numbers[-1]) # 5
```

We can also create nested list in which each element itself is one-dimensional list.

```python
nested_list = [[1, 2], [3, 4]]
print(nested_list[0]) # [1, 2]
print(nested_list[0][1]) # 2
```

## List Slicing

We can perform list slicing operations to get a sub-list. This is based on list indices, so again knowledge of indices comes into play. It again works on the same slicing operations like string datatype. We use square brackets to specify the start and end position. The general syntax for slicing operation looks like this.

```python
lst[start:stop:step]
```

In slicing operation, the `start` index element is included and `stop` index element is excluded in the output list. 

**Example:**

```python
numbers = list(range(1,11))
print(numbers[4:6]) # [5, 6]
```

If we don't specify start position, it by default starts from the beginning of the list at position `0`. If we don't specify the stop position, it goes upto the end of the list, i.e. `len(lst) - 1`.

```python
print(numbers[:3]) # [1, 2, 3]
print(numbers[5:]) # [6, 7, 8, 9, 10]
```

By default, the step value is `1`, but we can specify different value in the third number in square brackets. We can also omit any of the other values. For example, to get only even numbers from the above `numbers` list, we can specify `step` value as `2`.

```python
print(numbers[1::2]) # [2, 4, 6, 8, 10]
```

Based on List slicing, there is a neat trick to reverse a list.

```python
print(numbers[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

We can combine two lists using `+` operator.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2) # [1, 2, 3, 4, 5, 6]
```

## Unpacking lists

List unpacking is little different from other programming languages. If you've background in Javascript then you may find it similar destructing assignment.

In the below code, I have simple list with two values and in the second statement, I'm assigning those values to variables `a` and `b` respectively.

```python
lst = [1,2]
a, b = lst
print(a,b) # 1 2
```

In this, we can assign values from list into multiple variables on the left. We have to make sure to have equal number of variables on the left hand side as the number of elements in the list. If these don't match, it throws an error.

```python
a, b, c = lst # ValueError: not enough values to unpack (expected 3, got 2)
```

## Iterating through List

Lists are iterable and we can iterate through each element of the list using for loop.

**Example:**

```python
fruits = ["apple", "orange", "banana"]

for fruit in fruits:
    print(fruit)
```

**Output:**

```output{ lineNos=false }
apple
orange
banana
```

If we also need the index of each element, we can use the built-in [enumerate function](https://docs.python.org/3/library/functions.html#enumerate). This function returns a tuple containing index and the actual value obtained by iterating through the list.

**Example:**

```python
cities = ["New York", "London", "New Delhi", "Sydney"]

for index, city in enumerate(cities):
    print(f"City {index}: {city}")
```

**Output:**

```output{ lineNos=false }
City 0: New York
City 1: London
City 2: New Delhi
City 3: Sydney
```

## List Methods

There are lots of built-in methods that we can use to manipulate lists. Methods are similar to function but they work on specific data types. In this case, they work on lists. Methods are usually invoked using dot (`.`) notation. We specify list followed by dot and then the method name.

### Inserting elements

We can insert elements into a list using `insert` method which takes the position where we want to insert new element and the element we want to insert.

```python
numbers = [0, 1, 2, 3]
numbers.insert(4, 400)
print(numbers) # [0, 1, 2, 3, 400]
```

We can append an element at the end using `append`

```python
numbers.append(400) # [0, 1, 2, 3, 400]
```

### Removing Elements

We can use `pop` to pop out an element from the list and return it. The `pop` function can also take an index to remove the element from a specific index position.

```python
last = numbers.pop()
print(last) # 400
print(numbers) # [0, 1, 2, 3]
numbers.pop(2)
print(numbers) # [0, 1, 3]
```

We can also use `del` operator to remove an element from the list. This does not return that element, it only removes it from the list.

```python
del numbers[-1]
print(numbers) # [0, 1]
```

If we want to remove specific element by value, we can use `remove` method. This takes the element to remove and not the index position unlike `pop` method. Also, if there are multiple occurrences of the same element, it will remove only the first instance of that element.

```python
numbers = [1, 2, 3, 400, 5, 400]
numbers.remove(400)
print(numbers) # [1, 2, 3, 5, 400]
```

### How to Join Python lists

As we saw previously, we can append two lists using `+` operator. This returns new list and does not modify existing one.

```python
numbers = [1, 2, 3]
others = [4, 5, 6]
print(numbers + others) # [1, 2, 3, 4, 5, 6]
print(numbers) # [1, 2, 3]
print(others) # [4, 5, 6]
```

If we want to modify existing list, we can use `extend` method which takes another list as argument.

```python
numbers = [1, 2, 3]
others = [4, 5, 6]
numbers.extend(others)
print(numbers) # [1, 2, 3, 4, 5, 6]
```

### How to compare Python Lists

We can compare two lists using `==`. This checks each list elements and if they are all equal, then only this returns `True`.

```python
numbers = [1, 2, 3]
others = list(range(1, 4))
another = list(range(3))
print(numbers) # [1, 2, 3]
print(others) # [1, 2, 3]
print(another) # [0, 1, 2]
print(numbers == others) # True
print(numbers == another) # False
```

These are two separate instances of lists. We can verify this by checking their object id using `id()` function. This will give different result every time we execute it.

```python
print(id(numbers)) # 2074723580608
print(id(others)) # 2074720324800
```

### How to find elements in a List

To find specific element from a list, there are multiple options.

1. Iterate through the list and search for that specific item. This is not so useful as there are better methods mentioned below.
2. Use the `index()` method to find given element.
3. Use `in` operator.

```python
fruits = ["apple", "orange", "banana"]
banana_index = fruits.index("banana")
print(banana_index) # 2
```

If the list does not contain an element we are trying to index, then index method throws `ValueError`.

```python
fruits.index("pineapple") # ValueError: 'pineapple' is not in list
```

There is much better option to find elements in a list using `in` operator. This does not throw error when element is not found in the list and is the most preferred method for searching a list. This returns boolean result whether the item exists or not.

```python
fruits = ["apple", "orange", "banana"]
"apple" in fruits # True
"pineapple" in fruits # False
```

To avoid this error with `index()` method, we have to check whether an item exists before getting the index position of the element.

```python
pineapple_position = fruits.index("pineapple") if "pineapple" in fruits else -1
print(pineapple_position) # -1
```

### How to sort List elements

Lists can be sorted using built-in function `sorted()`. This returns a brand new list with elements sorted in ascending order by default.

```python
fruits = ["apple", "orange", "banana"]
print(sorted(fruits)) # ['apple', 'banana', 'orange']
print(fruits) # ['apple', 'orange', 'banana']
```

If we want to sort the existing list in-place, we can invoke a method `sort()` on that list. This function returns `None`.

```python
fruits = ["apple", "orange", "banana"]
fruits.sort()
print(fruits) # ['apple', 'banana', 'orange']
```

If we want to create a reverse list, we could pass keyword argument `reverse=True` to this `sort()` method. If we don't want to modify existing list, we can call `sorted()` function with `reverse=True`.

```python
fruits = ["apple", "orange", "banana"]
sorted_fruits = sorted(fruits, reverse=True)
print(sorted_fruits) # ['orange', 'banana', 'apple']
print(fruits) # ['apple', 'orange', 'banana']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'banana', 'apple']
```

### Other Functions

We can repeat elements of a list type by `*` operator.

```python
numbers = [1, 2, 3]
print(numbers * 2) # [1, 2, 3, 1, 2, 3]
```

There are built-in functions to find `sum`, `max` and `min` from a list.

```python
numbers = [1, 2, 3]
print(sum(numbers)) # 6
print(min(numbers)) # 1
print(max(numbers)) # 3
```

We can create a string from a list of string by joining all elements with a separator using `join()` function from string.

```python
fruits = ["apple", "orange", "banana"]
all_fruits = ", ".join(fruits)
print(all_fruits) # apple, orange, banana
```

Similarly, we can split a string and create a list of string by splitting a list with specific delimiter using `split()` method on string.

```python
colors = "red, black, white".split(", ")
print(colors) # ['red', 'black', 'white']
print("one-two-three".split("-")) # ['one', 'two', 'three']
```

We can clear all elements of a list using `clear()` method.

```python
numbers = [1, 2, 3]
print(numbers) # [1, 2, 3]
numbers.clear()
print(numbers) # []
```

## List Comprehension

List comprehensions provide succinct way to write loops and other list manipulations. This looks like below.

```python
[expression for elem in list]
```

Let's see how we write loops and then we will try to convert that to list comprehension.

```python
fruits = ["apple", "orange", "banana"]
# Create list with only first character from above fruits list.
lst = []
for fruit in fruits:
    lst.append(fruit[0])
print(lst) # ['a', 'o', 'b']
```

This could be converted into list comprehension like this.

**Example:**

```python
fruits = ["apple", "orange", "banana"]
lst = [fruit[0] for fruit in fruits]
print(lst) # ['a', 'o', 'b']
```

Similarly, let's say we have numbers list and we want to create another list whose elements are going to be the square of the original list. We could do that using loop or list comprehension.

Below is normal way to do it using loop.

```python
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number * number)
print(squares) # [1, 4, 9, 16, 25]
```

Using List comprehension it looks like this.

**Example:**

```python
numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
print(squares) # [1, 4, 9, 16, 25]
```

We can also include simple conditionals in list comprehension to filter out certain elements of the source list. Below is an example of creating new list with only squares of even numbers from another list containing even and odd numbers.

```python
numbers = [1, 2, 3, 4, 5]
even_squares = [number * number for number in numbers if number % 2 == 0]
print(even_squares) # [4, 16]
```