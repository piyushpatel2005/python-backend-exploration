# Python Functions

Functions are reusable code blocks that we can define once and reuse multiple times. These allows us to modularize our code where a function does one thing well. We have already used `print` function. Let's see how we can define our own functions.

## Overview

As I already mentioned, functions are reusable code  blocks which perform specific task. We can customize function behaviour by passing parameters into it. Depending on values of the parameters, it can perform different actions. We will take a look at such examples.

## General Syntax

Python syntax for defining function looks like this.

```python
def <function_name>:
    # body of the function
```

- Functions are defined using `def` keyword
- Function names have similar naming convention as variables. They should be using snakecase naming convention.
- Function can take parameters but it's not mandatory. These are values passed into the function which can be used by the function.
- The function body can contain one or more statements. Function block is created using indentation.
- Functions can have return statement at the end. If not return statement is used, it by default return `None`. We will see this in detail in example.
- We can define function doc string using triple quotes.

Let's define a simple function

### Defining and Calling a Function

```python
def greet():
    print("Hello")
```

Here, we have defined a function called `greet` which prints `Hello` on the console. After function name `greet` we have pair of parentheses. This is where it can take function arguments as we will see in next example. Now, to call this function, we have to use function name and pair of parentheses. Also, we can call the same function multiple times and it will give this result as many times as we call the function

```python
def greet():
    print("Hello")

greet()
greet()
```

```output{ lineNos=false }
Hello
Hello
```

### Define and Use a Function with Parameters

Now, this `greet` function is very limiting. It does only one kind of greeting and there is no customization. We can pass arguments to make it more useful.

```python
def greet(name):
    print("Hello", name)

greet("John")
greet("Rebecca")
```

Here, we pass `name` as one of the parameters and it will greet that person.

**Output**
```output{ lineNos=false }
Hello John
Hello Rebecca
```

{{< admonition >}}
**Parameters** are the names we use in the function definition. When function is called, what we pass in that function call is called **arguments**. These two look very similar, but different names might be confusing.
{{< /admonition >}}

## Doc String

Let's take a look at what is doc string in Python. We can define functions but to make them reusable, we have to provide some information to other developers. Usually, this information will be shared in the form of doc strings. For example, we can define doc string for our lovely `greet` function.

```python
def greet(name):
    """
    prints greeting message for a person
    ------------------------------------
    
    name: a string representing the name of the person
    """
    print("Hello", name)

help(greet)
```

Python has built-in function `help` which is used by many developers to find help on any function. Now, if we check `help` on our function, it will give us information about our function like this.

```console{ lineNos=false }
Help on function greet in module __main__:

greet(name)
    prints greeting message for a person
    ------------------------------------

    name: a string representing the name of the person
```

This can be informative for other developers as they can see what this function does in plain English and will not have to read through function definition. This can be very useful especially for large functions where reading code might be little bit difficult than reading this doc string.

## Return statement

Functions can also return a value. 
For functions to be useful, it has to return some values when we pass any arguments into it. This is how functions can help simplify our code. If the code file was just a single large code in sequence, it will be very difficult to remember every variable and follow through the code. Instead of this, if the code was divided into functions, it can be easier to remember what each function does (usually name should clearly reflect this) and follow the code. For simple, case let's see a function which does just one thing, add two numbers.

```python
def add (a, b):
    sum = a + b
    return sum
    
sum_of_two_numbers = add(2, 3)
print(sum_of_two_numbers)
```

In this function, we define a variable `sum` which calculates the sum of two variables and finally we use `return` to return this calculated sum. When we return this value, it gets replaced where we called the function (on line 5). Hence, the value assigned to variable `sum_of_two_numbers` is `5` and it prints `5`.

So, what happens when we don't return any value explicitly. For example, our `greet` function? In that function, we did not write any `return` statement.

```python
print(greet("Rocky"))
```

**Output**
```output{ lineNos=false }
Hello Rocky
None
```

In Python, function can also return multiple values unlike some other languages. For example, let's define a function which returns quotient and remainder of a division operation

```python
def div_mod(a, b):
    """
    This function takes two arguments and returns quotient and remainder of the division operation as `int`
    """
    division = a // b
    remainder = a % b
    return division, remainder

print(div_mod(5,2))
```

These values are returned as [tuples](../tuples/) which we will see in later lesson.
```output{ lineNos=false }
(2, 1)
```

## Default Arguments

In Python function, we can also provide default values for arguments. When a function is called without those parameters passed, the function takes default value as an argument.

```python
def greet(name='buddy'):
    return "Hello, " + name + "!"

print(greet("Bob"))
print(greet())
```

Even thoough, we have not passed any argument into `greet` function on line 5, the function returns greeting with default name as `buddy`.

**Output:**
```output{ lineNos=false }
Hello, Bob!
Hello, buddy!
```

Similarly, we can modify the greeting too with another parameter `greeting`.

```python
def welcome(greeting="Hello", name="Sir"):
    return greeting + ", " + name + "!"

greetings = welcome("Good morning", "Bob")
print(greetings)
```

**Output:**
```output{ lineNos=false }
Good morning, Bob!
```

When providing default arguments, the default argument must be the last argument in the function. So, function declaration like `def welcome(greeting="Hello", name)` would throw an error.

## Keyword arguments

One issue with above code is that if I pass the arguments in the function in reverse order then the function gives awkward result.

```python
greeting("Bob", "Hello")
```

**Output:**
```output{ lineNos=false }
Bob, Hello!
```

This gives inappropriate message. To resolve this, we can provide keywords which are same name as the function parameter name. This way Python interpreter will pass correct value in the correct argument. Note the  function is defined with order of arguments in different order.

```python
greeting(name="Bob", greeting="Hello")
```

This gives correct result.

**Output:**
```output{ lineNos=false }
Hello, Bob!
```

## Conclusion

In this lesson, we looked at how to define function and how to use those functions by calling them. We also saw how we can customize the function behaviour using arguments. Doc strings help provide documentation on functions we define. Functions can also return values using `return` keyword which makes functions reusable. We also saw how keyword arguments and default arguments can be useful to provide default arguments to a function and make the function more readable.