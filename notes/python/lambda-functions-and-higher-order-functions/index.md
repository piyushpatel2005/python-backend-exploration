# Lambda Functions and Higher Order Functions

Lambdas are derived from mathematical concept of lambda calculus. These are very important construct of a programming language to support Functional programming. Python, Java, C# and other languages have lambdas added to their syntax to facilitate new style of programming. 

## Lambda Functions

If have have a simple function, we can easily transform that function into **lambda function**. Lambda functions are also called anonymous functions because they are not assigned any explicit name. This is actually converted into same Python byte code, but it can be succint and because these functions will be used once only, there is no reason to name these kinds of functions.

Let's learn from a simple example.

```python
def square(x):
    return x * x
print(square(2)) # 4
```

We can write this as a lambda function.

```python
lambda_square = lambda x: x * x
print(lambda_square(2)) # 4
```

- Lambda functions tend to be quite succinct. 
- They can be used when we want to use a function only once. 
- Usually, lambda functions are used with other higher order functions.

## Higher Order Functions

Higher order functions are functions that take other functions as their parameters. We can also pass a function as an argument while calling another function. In Python, everything is an object, even functions. We have higher order functions `map`, `filter` and several other functions from `functools` module. Module is simply a Python source file available for us to use.

Let's learn about these functions one by one.

### Map 

The `map` function can be used when we want to map our collection datatype to some other values. We can think of this as transforming our container datatype into some other container datatype. The easiest example would be imagine that we have a list of string datatype and we want a list with length of each of those list elements. This could be easily accomplished using `map` function. This function takes a lambda which is the operation we want to perform on each element of the source list. This function returns an iterable which we have to convert to list using `list()` function.

**Example:**

```python
names = ["Anil", "Alex", "Jennifer"]
length_of_names = list(map(lambda x: len(x), names))
print(length_of_names)
```

Map operation always returns an object with same number of elements. 

**Output:**

```output{ lineNos=false }
[4, 4, 8]
```

### Filter

If we want to select only specific elements from our original list, then we can use the higher order function `filter` for this. `filter` function also looks similar to `map` function, but the lambda function we pass into this function will be returning result of boolean type. Whenever that lambda returns `True`, those values will be included in the returned iterable.

Let's imagine that we want to get all names that start with character `A`, then we can use `filter` operation to verify the first character as shown below.

Again, this function does not return `list`, but it returns an iterable. We can convert it to any other container datatype. So, let's cast it to a `list`.

**Example:**

```python
names = ["Anil", "Alex", "Jennifer"]
filtered_names = list(filter(lambda name: name[0] == "A", names))
print(filtered_names)
```

**Output:**

```output{ lineNos=false }
['Anil', 'Alex']
```

## Practical Use of Map, Filter

Let's see one practical some use case of these functions.

Let's say, we want to get salaries of each of these `users` in a separate list and we want to create some form of chart using those `salary` values, then we can get them using `map` function and a lambda expression.

**Example:**

```python
users = [
    {
        "name": "Alex",
        "age": 23,
        "profession": "Software Developer",
        "industry": "Information Technology",
        "salary": 50000
    }, 
    {
        "name": "Neha",
        "age": 27,
        "profession": "Accountant",
        "industry": "Finance",
        "salary": 55000
    },
    {
        "name": "John",
        "age": 38,
        "profession": "Plant Manager",
        "industry": "Manufacturing",
        "salary": 75000
    },
    {
        "name": "Salman",
        "age": 32,
        "profession": "Banker",
        "industry": "Finance",
        "salary": 43000
    },
    {
        "name": "Steve",
        "age": 29,
        "profession": "Software Architect",
        "industry": "Information Technology",
        "salary": 61000
    }
]

salaries = list(map(lambda user: user["salary"], users))
print(salaries)
```

**Output:**

```output{ lineNos=false }
[50000, 55000, 75000, 43000, 61000]
```

Similarly, if I want to get all the users who work in the `Information Technology` field, we can use the `filter` function for that. For the sake of brevity, I have omitted `users` variable initialization in below snippet.

```python
infotech_users = list(filter(lambda user: user["industry"] == "Information Technology", users))
print(infotech_users)
```

We can also chain these operations. Let's say, I want to get only salaries of only those working in `Information Technology`. In that case, I can first select users who are into `Information Technology` and then we can find their salaries. The first subtask could be achieved using `filter` function and the second one could be achieved using `map` function. This will report only two `user`'s salaries.

**Example:**

```python
it_salaries = list(
    map(
        lambda user: user["salary"], 
        filter(
            lambda user: user["industry"] == "Information Technology", 
            users
        )
    )
)
print(it_salaries)
```

**Output:**

```output{ lineNos=false }
[50000, 61000]
```

In above examples, we are passing computation in the form of lambda functions. This style of programming are also reffered to as **functional programming**. This is widely used in data analytics and data engineering with frameworks like Spark.

### Reduce

There is also `reduce` function if you want to find the aggregated values. This function is available in separate module `functools` in Python 3, so we first need to import it.

**Example:**

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda sum, x: sum + x, numbers)
print(sum) # 15
```

When we use `reduce()` function on empty sequence with no initial value, it will throw an error.

```python
from functools import reduce
numbers = []
sum = reduce(lambda sum, x: sum + x, numbers)
print(sum) # TypeError: reduce() of empty sequence with no initial value
```

To avoid this, `reduce` method also takes third optional argument with initial value. It's always better to specify this initial values to cover corner cases like this one.

**Example:**

```python
from functools import reduce
numbers = []
sum = reduce(lambda sum, x: sum + x, numbers, 0)
print(sum) # 0
```

If I write any other default value, then it will use that initial value for this `sum` variable. For instance, in below code, I have included initial value of `10`, then it will perform operation as `(((10 + 1) + 2) + 3)`.

```python
from functools import reduce
numbers = [1, 2, 3]
sum = reduce(lambda sum, x: sum + x, numbers, 10)
print(sum) # 16
```

If I want to find the product of all elements of a list, then I just have to modify the computation I need to perform.

```python
from functools import reduce
numbers = [1, 2, 3]
product = reduce(lambda prod, x: prod * x, numbers, 1)
print(product) # 6
```

Let's make use of our this `reduce` function for larger problem. We want to find sum of salaries for all `users` who are over `30` years old. We can first `filter` elements with age over `30`, then `map` those users to their salaries and finally we can calculate the sum of `salary` using `reduce` function.

**Example:**

```python
users = [
    {
        "name": "Alex",
        "age": 23,
        "profession": "Software Developer",
        "industry": "Information Technology",
        "salary": 50000
    }, 
    {
        "name": "Neha",
        "age": 27,
        "profession": "Accountant",
        "industry": "Finance",
        "salary": 55000
    },
    {
        "name": "John",
        "age": 38,
        "profession": "Plant Manager",
        "industry": "Manufacturing",
        "salary": 75000
    },
    {
        "name": "Salman",
        "age": 32,
        "profession": "Banker",
        "industry": "Finance",
        "salary": 43000
    },
    {
        "name": "Steve",
        "age": 29,
        "profession": "Software Architect",
        "industry": "Information Technology",
        "salary": 61000
    }
]

filtered = filter(lambda user: user["age"] > 30, users)
salaries = map(lambda user: user["salary"], filtered)
sum_of_salaries = reduce(lambda sum, salary: sum + salary, salaries, 0)
print(sum_of_salaries) # 118000
```

We could also chain these operations like we saw earlier and it would have produced the same output. This looks little more readable.