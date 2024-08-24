# Sets in Python

Sets are another collection datatype which contains unordered elements. These elements cannot be indexed like lists or tuples. Sets are mutable. So, we can add or remove elements.

We can perform set theory operations like we studied in mathematics in high school: union, intersection, symmetrical difference, etc.

## Creating Sets

We can creates a set using curly braces (`{}`). We could also use `set()` function to create a set from any iterable. It is an object of type `set`.

For creating empty set, we have to use `set()` function. We cannot use `{}` for creating empty set. This is because the later symbol is reserved for creating empty dictionary. We will learn about this data structure in the next lesson.

```python
# Empty sets
empty_set = set()
type(empty_set) # set

numbers = {1, 2, 3, 4, 5}
print(numbers) # {1, 2, 3, 4, 5}

numbers = set(range(5))
print(numbers) # {0, 1, 2, 3, 4}
```

Sets are unordered collection. It means they cannot be indexed like lists or tuple. If we try to get an item from specific index, we get `TypeError`.

```python
numbers = {1, 2, 3, 4, 5}
print(numbers[1])
```

**Output:**

```output{ lineNos=false }
TypeError: 'set' object is not subscriptable
```

We can add an element to existing set using `add` method and remove an element using `remove` method.

```python
colors = {"black", "white", "blue"}
colors.add("red")
print(colors)
colors.remove("black")
print(colors)
```

**Output:**

```output{ lineNos=false }
{'red', 'white', 'black', 'blue'}
{'white', 'blue', 'red'}
```

One of the important properties of sets is that it cannot have duplicates. If I try to add an element twice, it will simply discard that element and will not add to existing set.

**Example:**

```python
colors = {"black", "white", "blue"}
print(colors)
colors.add("red") # correctly adds this color
print(colors)
colors.add("white") # does not add 'white' second time
print(colors)
```

**Output:**

```output{ lineNos=false }
{'white', 'black', 'blue'}
{'red', 'white', 'black', 'blue'}
{'red', 'white', 'black', 'blue'}
```

Once we have sets, we can perform different set theory operations on them.

We can find **union** of two sets. This will simply merge the elements of two sets. We can also use `|` symbol for this operation.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7}
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7}
```

We can find intersecting elements using **intersection** operation. This returns only the common elements between two sets.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1.intersection(set2)) # {4, 5}
print(set1 & set2) # {4, 5}
```

We can also find the **difference** of two sets. This will return the difference of two sets. It will return elements which are in first set, but not in the second one.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1.difference(set2)) # {1, 2, 3}
print(set1 - set2) # {1, 2, 3}
```

We can find **symmetrical difference** of two sets. This will return all the elements from both sets which are present in one of the sets but not both.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print(set1.symmetric_difference(set2)) # {1, 2, 3, 6, 7}
print(set1 ^ set2) # {1, 2, 3, 6, 7}
```
We can find out if two sets are **disjoint** sets. These are sets which have no matching elements between them.

```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) # True
```

We can validate if a set is subset of another set. This will return `True` if all elements are present in the given set. Similarly, we can use issuperset method to check the reverse of issubset method.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
set3 = {4, 5}
print(set1.issubset(set2)) # False
print(set3.issubset(set2)) # True
print(set1.issuperset(set2)) # False
```

We can clear all elements of a set using `clear()` method. It will remove all elements from the set.

```python
numbers = {1, 2, 3}
print(numbers) # {1, 2, 3}
numbers.clear()
print(numbers) # set()
```