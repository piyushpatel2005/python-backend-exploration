# String Formatting in Python

There are several ways to print statements in Python. We will see different ways to print values in using print statements including modern **string interpolation**. We will see four different methods for Python string formatting.

## Overview

We will cover four different methods for formatting strings.

1. Concatenation using `+` Operator
2. Printf-style String formatting
3. Format method
4. f-String Interpolation

## Using + Operator

We can print individual variables using their varible name like below.

```python
greeting = "Welcome"
name = "John"
print(greeting)
print(name)
```

This will print `Welcome` and `John` on two separate lines. What if we want to print them in single line like `Welcome John`?

The most basic method of writing multiple values in Python is by using `+` operator or also called string concatenation variable.

```python
greeting = "Welcome"
name = "John"
print(greeting + " " + name)
```

```output{lineNos=false}
Welcome John
```

This works well, but if there are variables of data type other than string then it becomes tedious. For example, below errors out.

```python
name = 'John'
age = 23
print("Hello, I'm " + name + " and I'm " + age + " years old.")
```

```output{ lineNos=false }
TypeError: can only concatenate str (not "int") to str
```
The problem is that `age` is of type `int` and Python concatenation operation fails to concatenate string with integer variable. In order to make it work, we have to `cast` integer value to string type. Just change last line to this where we convert `age` to string type using `str(age)`.

```python
print("Hello, I'm " + name + " and I'm " + str(age) + " years old.")
```

```output{ lineNos=false }
Hello, I'm John and I'm 23 years old.
```

Also, something else to note is that, when we have to use single quote inside the string, it's best to use double quotes to start the string otherwise we may have to escape single quotes like this. The character `\` is used to escape the next character after slash.

```python
print('Hello, I\'m ' + name + ' and I\'m ' + str(age) + " years old.")
```

Similar to this single quote escaping, we have to escape double quotes if those are being used inside a string which starts with double quotes.

### What is Casting

Casting is converting one data type into another. It tries to convert whether it can be converted or not. If it cannot be converted, it will fail with an error. In Python, casting is very simple, we just have to use the function with the type we want to convert to.

```python
int(32.99) # convert float to int => 32
float(2) # cast int to float => 2.0
str(32.99) # cast float to str => '32.99'
str(23) # cast int to str => '23'
```

## Printf style String formatting

Python also has C-style printf formatting which uses format specifier to print variables or values.
Let's take the same example, but with printf style string formatting.

```python
name = 'John'
age = 23
print("Hello, I'm %s and I'm %d years old." %(name, age))
```

Here, we have replaced string value `name` with `%s` and integer value `age` with `%d` format specifier. These are used to represent string and integers respectively. After the statement, we provide those arguments inside `%()` in the same sequence as the one in which they appear in the text. Also, if one of the arguemnts is missing, then also this `print` operation will fail. 
There are several format specifiers. Some of the most common ones are as below. 

| Format Specifier | Description |
|:-----------------|:------------|
| `%d` | Integer |
| `%f` | Floating point number |
| `%S` | String |
| `%c` | Character |

The most interesting one is `%f` which allows us to also specify the precision of the number we are printing.

```python
gold_price = 98.589
print("The gold price is %.2f." %(gold_price))
```

This produces output with just 2 decimal points. It rounds the number to 2 decimal point and prints them.

```output{ lineNos=false }
The gold price is 98.59.
```

## Format method on string

String objects also have a format method, which takes number or arguments that we want to insert. The string we want to print will have placeholders using `{}` and those will be replaced by the arguemnts in the `format` method.

```python
business_name = 'ABC Corp.'
years_in_business = 20
print("{} has been in business for {} years".format(business_name, years_in_business))
```

```output{ lineNos=false }
ABC Corp. has been in business for 20 years
```

The interesting part of thie style of formatting string is that, we can also specify the different sequence of arguments. For example, we can pass `years_in_business` first as shown below. In this, we specify the placeholder with the argument number which should be placed in there using `{0}`.

```python
print("{1} has been in business for {0} years".format(years_in_business, business_name))
```

Alternatively, we could also specify the named arguments and those named arguments will replace the placeholder.

```python
print("{name} has been in business for {years} years".format(name=business_name, years=years_in_business))
```

Both these approaches produce the same output as the first one. We could also use the number formatting format floating point numbers.

```python
price= 99.99
print("I bought {0:.2f} dollars worth video games.".format(price))
print("I bought {price:.2f} dollars worth video games.".format(price=price))
```

```output{ lineNos=false }
I bought 99.99 dollars worth video games.
I bought 99.99 dollars worth video games.
```

## f-string Interpolation

With Python 3.6, there is yet another way to format strings easily. This is using **String Interpolation** using f-strings. This is relatively straight-forward and perhaps the most widely used method for formatting strings. We just use character `f` before starting the string and then inside the string we can simple refer to variables using curly braces `{}`. Again, this also allows for floating-point number formatting like `format` method.

```python
name = 'John'
age = 23
price = 49.44
print(f"Hello, I'm {name} and I'm {age} years old.")
print(f"I also bought {price :.1f} worth books.")
```

```output{ lineNos=false}
Hello, I'm John and I'm 23 years old.
I also bought 49.4 worth books.
```

## Conclusion

In this lesson, we looked at four different string formatting methods in Python. These included concatenation operator, printf-style string formatting using `%` sign, `format` method and the latest one f-string interpolation. f-string interpolation is the most preferred method for writing string because it is concise and very readable in Python community.