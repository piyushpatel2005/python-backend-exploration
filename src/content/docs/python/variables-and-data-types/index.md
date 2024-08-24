---
title: "Variables and Data Types in Python"
date: 2023-07-24T13:27:37-04:00
draft: false
keywords: ['what are variable', 'data types in python', 'variable declaration and initialization', 'python syntax for variables', 'snake case in python', 'variable naming convention in python', ]
---

In this lesson, let's take a look at what is variable in Python and what are different data types available with Python including collection types.

<!--more-->

## What are variables?

Variables are just a placeholder that can hold some data. The data is stored in computer memory in the form of bits. However, those memory addresses are difficult to remember. So, variables provide a name for those variable addresses in the memory. Creating variables in Python is relatively straight forward. The general syntax for variable declaration and initialization looks like this.

```python
<variable_name> = <value>
```

Unlike few other programming languages, Python does not require the developer to explicitly specify the data type of the variable which makes coding in Python relatively simpler. 

Variables in Python are named using *snake-case*. That is if the variable name contains multiple words, they are separated by underscore(`_`). The variable names must follow certain conditions.

1. The nmae can start with upper case or lower case alphabetic characters.
2. All variable names are case-sensitive. That means variable `is_adult` is not the same as `is_Adult`.
3. Variable name must not contain any of the language keywords. These are words like `True`, `False`, `if`, `import` etc. We will see them as we learn Python further.
4. Variable name can include numbers but that must not begin with a number. So, variable name like `21joseph` is not a valid variable name but `joseph21` is a valid one.
5. Spaces are not allowed in variable name and for better readability the variable names should be informative or descriptive. So, rather than creating variables like `a`, `b`, use words like `acceleration` or `begin_time`. Again, depending on context, you may have to make it more descriptive than this.

## Data Types

There are three main data types. These include

1. **Numbers**

    Numbers are further divided into following.
    - *Integers*: represents whole numbers
    - *Float*: These are numbers with decimal values.
    - *Complex numbers*: These are mostly used in mathematics.
2. **String**: Text data. These are created using `'` (single quote), double quote `"` or triple quote which is three times single quote or double quote like `"""` or `'''`.
3. **Booleans**: These are used to represent conditionals or 'Yes', 'No' kind of situations.

In below code snippet, I have declared variables of type `string`, `int`, `float` and `boolean` and we can print all of these variables using the same `print` function by passing the variable name into it.
There is also something else starting with hash or pound symbol (`#`). This is called comment in Python. Comment basically means everything written after this character on a line will be ignored. These are only used as a code logic explanation for other programmer's readability.

```python
name = "Alex" # string variable
age = 32 # int variable
salary = 4578.78 # float variable
is_married = True # boolean variable
print(name)
print(age)
print(salary)
print(is_married)
```

As you can see, `string` data type, we can use either single quote (`'`) or double quotes (`"`) like I have used. For `boolean` data type, we use `True` or `False` keywords with first letter capitalized.

If I execute this code, it prints below.

```shell{ .show-prompt lineNos=false }
python main.py
```

```console{ lineNos=false }
Alex
32     
4578.78
True
```

We can also declare multiple variables on a single line and the values will be assigned in the same sequence as the variables on the left.

```python
a, b, c = 10, "Hello", 10.2
print(a) # 10
print(b) # Hello
print(c) # 10.2
```

If we want to check the data type of each of these variables, we can look up their type using `type` built-in function. We will learn more about `function`s later in a separate lesson, but for now, this is how we use it.

```python
a, b, c = 10, "Hello", 10.2
print(type(a))
print(type(b))
print(type(c))
```

```output{lineNos=false}
<class 'int'>
<class 'str'>
<class 'float'>
```

It types keyword `class` and the type of the variable. This can become useful when debugging code.

### None value

Python also has a special value called `None`. This is used to define absense of any value for an object. This is similar to `null` in other programming languages. We can assign `None` value to any variable and this value has a type `NoneType`. Few key points about this value are:
- `None` is not exactly same as `False` even though in [conditional check](../conditionals/#conditionals-with-none) it acts like a falsy value.
- Similarly, `None` is not `0` nor an empty string.

### Python Collections.

On top of these base data types, we also have collection data types. In general, when we want to store data, we will be storing data as a collection. For example, a collection for user grades, a collection of employee records, a collection of course names, etc. In order to store that we have three main types of collections.

1. **List**: This is a collection where each individual element is of the same type. They are usually created using double brackets (`[]`). For example, array of grades look like `[60, 70, 80]`
2. **Tuple**: This is an immutable collection where we cannot add or delete an element from it. In terms of functionality, it is similar to list except that it can hold data of different types. These are created using double parentheses `()`.
3. **Sets**: This is used to store unique items. If we try to store the same item again, it will be discarded. This is created using `set()` function.
4. **Dictionaries**: These are key-value pairs. This is also known as hash map or associative array in other languages. They are created using `dict()` function or in short-hand using double curly braces (`{}`). Dictionary of user "John" looks like this. `{first_name: 'John', last_name: 'Doe', age: 20}`

We will cover these types in lot more details in their separate lessons.

## Conclusion

In this lesson, we learned about how to declare and initialize variables. We also saw how we can check the data type of a variable using `type` function. We learned about various data types available in Python and how to assign values to them. Finally, we had a brief introduction to collection data types which are used to hold a group of values.