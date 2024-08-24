# Error Handling

Python Error handling allows us to write code which will be fault-tolerant and still provide most relevant information when any error occurs. Errors are unavoidable, but we have to handle errors gracefully and provide proper logging information in order to debug error scenarios.

## Overview

When we are writing code, we will often come across errors that we didn't expect. This can be `SyntaxError` where we are writing code that Python doesn't know how to interpret or it could be a runtime error where our logic is getting unexpected input and it is failing. When an error occurs, Python interpreter will stop the execution of the current thread (process). we have already seen few errors in this tutorial. We saw `NameError` when Python doesn't know about a variable we are trying to access. We saw `KeyError` when we are trying to access the value for a key that doesn't exist in the dictionary. Similarly, there are many different types of errors we may get. We can also define our own custom error types.

We don't want our program users to see this kinds of nasty looking error stack traces. To avoid that, or even better, to properly handle the case where the error occurred, we can use error handling. The errors are also referred to as exceptions in other languages.

## Error Examples

If I try to concatenate string with integer values, Python interpreter will throw `TypeError` which means the data type of the two values do not match as expected.

**Example:**

```python
age = 21
print("My age is " + age)
```

**Output**

```output{ lineNos=false }
TypeError: can only concatenate str (not "int") to str
```

Most of the exceptions we will encouter are defined in the `builtins` module. You can find all the information about the built-in errors on [this page](https://docs.python.org/3/library/exceptions.html).
If we try to access an index of a tuple or list which doesn't exist, then we get `IndexError`.

```python
numbers = [1, 2, 3]
print(numbers[5])
```

**Output:**

```output{ lineNos=false }
IndexError: list index out of range
```

If we put incorrect indentation in any of the statement in our code file, we get `IndentationError`.

## Handling Exceptions using `try...except`

Python provides two keywords `try` and `except` to handle error cases. Exceptions can be handled using `try...except` statements. We wrap all the code that we want to execute inside the `try` block and if any of that code throws an error, the execution goes to the `except` block.

For example, below code produces `ZeroDivisionError` on line `2`. 

```python
a = 0
print (1 / a)
```

**Output:**

```output{ lineNos=false }
ZeroDivisionError: division by zero
```

To handle this error, we have to wrap it inside the `try` block. When this error occurs, the execution flow goes to `except` block where we can write meaningful message based on the error type.

**Example:**

```python
a = 0
try:
    print (1 / a)
except:
    print("Error occurred")
```

**Output:**

```output{ lineNos=false }
Error occurred
```

By default, `except` block will handle all kinds of error cases in the `try` block regardless of the error type. However, sometimes we want to handle errors differently based on what kind of error. This allows us to provide more accurate response for specific type of error our software encounters.

We can handle multiple different types of errors in `except` block. If we are taking user input then in those cases user can input any kind of data. At that time, we need to handle all those different scenarios in our exception handling code.

If we try to provide unexpected data type to any Python operation, that would result in `TypeError`. Let's take user input to calculate division of two numbers.

```python
print("Please, enter two numbers for calculating Division")
num1 = input("First number: ")
num2= input("Second number: ")

try:
    result = int(num1) / int(num2)
    print("Result of these two operations is " + result)

except ZeroDivisionError:
    print("Denominator cannot be zero for division.")
except TypeError:
    print("Make sure that you're concatenating two strings.")
except ValueError:
    print("Please, enter number and not string data.")
```

Below are various inputs we can provide and it handles the errors gracefully and sends relevant messages based on the error encountered.

If we pass input as `1` and `0`, we get `ZeroDivisionError` and we get corresponding message to fix this error.

```shell
python main.py      
```

```output{ lineNos=false }
Please, enter two numbers for calculating Division
First number: 1
Second number: 0
Denominator cannot be zero for division.
```

If we pass string as input instead of integer, we get relevant message with `ValueError`.

```output{ lineNos=false }    
Please, enter two numbers for calculating Division
First number: 1 
Second number: a
Please, enter number and not string data.
```

Finally, we encounter `TypeError` because in our code on line `7`, we are trying to concatenate `int` with `str` message.

```output{ lineNos=false }
Please, enter two numbers for calculating Division
First number: 1
Second number: 2
Make sure that you're concatenating two strings
```

Below is the corrected code.

```python
print("Please, enter two numbers for calculating Division")
num1 = input("First number: ")
num2= input("Second number: ")

try:
    result = int(num1) / int(num2)
    print("Result of these two operations is " + str(result))

except ZeroDivisionError:
    print("Denominator cannot be zero for division.")
except TypeError:
    print("Make sure that you're concatenating two strings.")
except ValueError:
    print("Please, enter number and not string data.")
```

We can also handle multiple errors in single `except` block like below snippet.

```python
try:
    result = int(num1) / int(num2)
    print("Result of these two operations is " + str(result))

except {ZeroDivisionError, TypeError, ValueError}:
    print("One of ZeroDivisionError, TypeError or ValueError occurred.")
```

Some of the most common types of built-in exceptions are listed below.

- `Exception`: This is base class for most of the Errors in Python.
- `ValueError`: This occcurs when a function receives an argument of unexpected type. This also occurs with operators in Python.
- `SyntaxError`: occurs when we have incorrect Python language syntax.
- `IndentationError`: occurs when we have inconsistent indentation in our source file.
- `ZeroDivisionError`: this is when we try to divide or try to find a module with denominator as zero.
- `NameError`: This occurs when a variable or name is not found in source file. This could be because we missed declaring a variable or if we miss importing a function or value.
- `ImportError`: This happens during importing a function or a class from a module. This could also be because that function or class is not defined in the module or we are missing a package installation. More details on this can be found in [Modules and Packages](../modules-and-packages/).
- `KeyError`: This is raised when a key is not found in dictionary.
- `OSError`: This occurs when a system level error occurs.
- `IndexError`: is raised when a sequence (list or tuple) is out of range in indexing or slicing.
- `IOError`: occurs when IO operation fails. This could be due to give filename not being available at a given location, but can also be due to other reason like file being  closed.

**Output:**

```output{ lineNos=false }    
Please, enter two numbers for calculating Division
First number: 1
Second number: 2
Result of these two operations is 0.5
```

There is also `else` block with `try...catch` but that's not used so much and it causes more confusion if ever used. So, below code is just to know the syntax incase you ever encounter it.

```python
lst = [1, 2, 3]
try:
    print(lst[2])
except IndexError:
    print("IndexError occurred.")
else:
    print(lst[len(lst) - 1])
```

**Output:**

```output{ lineNos=false }
IndexError occurred.
```

If error occurs, it executes only `except` block, but if error does not occur in `try` block, it will also execute `else` block after finishing `try` block.

## `finally` keyword

There is also `finally` block which will be executed no matter if error occurs or not. This can be useful in cases when we have to clear some resources from memory before we end our program. For example, when we are working with files, we have to make sure that we close the file before ending our code. If we open the file in `try` block and while reading this file, an error occurs, the execution moves to `except` block and that file may never be closed. Such cases can be handled using `finally` block. If we include file closing operation in the `finally` block, it will always be executed and file will always be closed regardless of whether an error occurs or not.

Let's write a file which can demonstrate this use-case. I have created a file with name `digits.txt` with content below.

```shell
cat digits.txt
```

```output{ lineNos=false }
1
2
a
```

In below code, it will throw an error while casting character a from the file into integer data type. If we look carefully at the execution, even if the execution goes inside the except block, our finally block is always invoked at the end.

```python
f = open("digits.txt")
sum = 0
try:
    print("Calculating sum")
    for line in f.readlines():
        num = int(line)
        sum += num
except:
    print("An error occurred")
    print("Sum: " + str(sum))
finally:
    print("Closing a file")
    f.close()
```

**Output:**

```output{ lineNos=false }
Calculating sum
An error occurred
Closing a file
```

If we modify the contents of the file `digits.txt`, then also the `finally` block gets executed as can be seen from the print statement in the output.

```shell
cat digits.txt
```

```output{ lineNos=false }
1
2
4
```

Executing this code again, produces below output

```output{ lineNos=false }
Calculating sum
Sum: 7
Closing a file
```

## `raise` keyword

If there are situations where we want to throw error without any actual error, then in that case we can use `raise` keyword. This may be useful to throw an error when our code cannot respond to certain user inputs. Below simple code snippet throws `ValueError` with custom error message.

```python
raise ValueError("This is wrong")
```

Let's say we have a use-case where we can add two numbers only when they are greater than `0` else we cannot perform operation, then we would like to check the user input and if it's negative, then we would like to `raise` an error.

**Example:**

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1 = int(num1)
num2 = int(num2)

if num1 < 0 or num2 < 0:
    raise ValueError("Numbers must be greater than zero.")
print("Sum: " + str(num1 + num2))
```

**Output:**

```shell
python main.py
Enter first number: 1
Enter second number: -1
```

```output{ lineNos=false }
ValueError: Numbers must be greater than zero.
```

I can use a `try...except` block to handle this case.

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    if num1 < 0 or num2 < 0:
        raise ValueError("Numbers must be greater than zero.")
    print("Sum: " + str(num1 + num2))
except:
    print("Something went wrong")
```
