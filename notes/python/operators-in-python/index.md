# Operators in Python

Operators are used to perform arithmetic and logical operations on input data. They allow us to manipulate data. They can be **in-fix** or **prefix** notations. In-fix ones appear between two operands (these are the values on which the operator works). A prefix operator usually works on one operand. These are also called binary and unary operators.

Operators can be classified into 5 different category. We will take a look at each of them one by one.

## Arithmetic Operators
This kind of operators allow us to perform arithmetic operations in Python. These include addition, subtraction, multiplication, division and few more. Below table summarizes these operators in detail.

| Operator | Description |
|:---------|:------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication of two numbers |
| `//` | Integer division. This returns the quotient of the division operation of two integers |
| `/` | Division. This returns float result for the division of two numbers. |
| `%` | This returns the remainder for the division of two numbers. This is also called modulo operator |
| `**` | Exponent. |

The easiest way to experiment with these operators is to use Python REPL (Read Evaluate Print Loop). On Command prompt, just type `python` and your prompt should change like below.

{{< admonition "note" >}}
Please, note that in REPL, it outputs the value directly without using any method like `print`. In actual code, we will have to use `print` function in order to print the output of the arithmetic operations.
{{< /admonition >}}

```shell{ .show-prompt lineNos=false }
python
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

```python
>>> 2 + 4 # sum of two numbers
6
>>> 4 - 2 # subtraction
2
>>> 2 - 5 # subtraction can return negative numbers too
-3
>>> 5 * 2 # multiplication
10
>>> 5 // 2 # integer division, returns quotient
2
>>> 5 % 2 # modulo, returns remainder of the division
1
>>> 5 / 2 # division
2.5
>>> 2 ** 3 # exponent 
8
>>>
```

## Assignment Operators
Assignment operators are used to assign values to a variable. The most common among these is `=` which we already used.

| Operator | Description |
|:---------|:------------|
| `=` | Assign a value to a variable |
| `+=` | Add and assigne a value |
| `-=` | Subtract and assgn a value |
| `*=` | Multiply and assign |
| `/=` | Divide and assign a value |
| `//=` | Divide and assign quotient |
| `%=` | Divide and assign remainder |
| `|=` | Bitwise OR and assign |
| `&=` | Bitwise AND and assign |
| `^=` | Bitwise XOR and assign |
| `>>=` | Bitwise Right shift and assign |
| `<<=` | Bitwise Left shift and assign |

```python
counter = 1
print(counter)

counter += 1 # 2
print(counter)

counter += 4 # 6
print(counter)

counter //= 2 # 3
print(counter)

counter %= 2 # 1
print(counter)
```

```output
1
2
6
3
1
```

## Comparison Operators

These are mathematical comparison operators. It returns boolean result based on the comparison operation being performed.

| Operator | Description |
|:---------|:------------|
| `>` | Greater than |
| `<` | Less than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |
| `!=` | Is not Equal to |
| `==` | Equal to |
| `is` | Verifies whether two objects are same |
| `is not` | Verifies whether two objects are different |

```shell{ .show-prompt lineNos=false }
python
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

```python
>>> 1 == 1
True
>>> 1 != 1
False
>>> 4 > 5
False
>>> 4 < 5
True
>>> 4 >= 4
True
>>> 6 <= 4
False
>>> 4 is 4 # This gives warning. We should be using variable instead of direct literal values.
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True
>>> num1 = 1 # create new variable
>>> num2 = 1 # create another variable with same value
>>> num1 is num2
True
>>> num1 is not num2
False
```
## Logical Operators
Logical operators are the ones which work on Boolean operands. These are also used in conditional checks usually along with comparison operators.

| Operator | Description |
|:---------|:------------|
| `and` | AND operation |
| `or` | OR operation |
| `not` | Complement operation |

Let's see an example of these operators

```python
is_logged_in = True
is_admin = False
print(is_logged_in and is_admin) # False
print(not is_admin) # True
print(not (not is_admin)) # False
print(is_logged_in and not is_admin) # True
```

```output{lineNos=false}
False
True
False
True
```

## Bitwise Operators

Bitwise operators work on bit level of data values. Each value is stored in the form of bits (0 and 1). These operators work on those bits. 

| Operator | Description |
|:---------|:------------|
| `&` | Bitwise AND operation |
| `|` | Bitwise OR operation |
| `^` | Bitwise XOR operation |
| `~` | Bitwise NOT operation |
| `<<` | Shift Left operation |
| `>>` | Shift Right operation |

```python
a = 4 # 0100
b = 2 # 0010
c = 5 # 0101
print(a | b) # 0110 = 6
print(a & b) # 0000 = 0
print(a ^ c) # 0001 = 1

print (b << 1) # 0100 = 4
print (b << 2) # 1000 = 8
print (c << 1) # 1010 = 10
```

```output{lineNos=false}
6
0
1
4
8
10
```

## Conclusion

In this lesson, we looked at what are different types of operators available in Python. We also looked at some of the constructs which can be used for conditional checks. Bitwise operators are used less but can become very useful for efficient algorithms.