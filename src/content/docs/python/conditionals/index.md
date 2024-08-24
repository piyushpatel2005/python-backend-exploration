---
title: "Conditionals in Python (If Else)"
date: 2023-08-02T06:59:03-04:00
draft: false
---

In any programming language, we will have few cases where we have to decide based on input to choose one of the paths. This is achieved using conditional statements or (`if..else`) blocks.

<!--more-->

Conditional statements (conditionals) are a way to make decisions. It offers opportunity to have multiple options for your program flow.

We can use `if...else` structure for different decisions. The structure of this conditional code blocks look like this.

```python
if condition:
    # ... .. ...
    # perform some actions
    # ... .. ...
else:
    # ... .. ...
    # perform other actions
    # ... .. ...
```

If you're coming from different programming language background, Python uses indentation for defining code blocks. Unlike other languages it does not use set of curly braces (`{}`) for this. So, in case of Python on line 1 above, `if condition:` starts a new block and everything within that `if` block is indented by 4 spaces. The number of spaces to indent can be whichever developer prefers but 4 spaces is the convention and it has to be consistent in a code file. This convention also helps in code readability.

## Practical Example
Let's take a very trivial example of `if..else` block.

```python
age = 10
if age > 18:
    print("You can drive")
else:
    print("You can't drive yet.")
```

In above code, we define variable on line 1. On line 2, we check if `age` variable is above 18. Depending on the value assigned to `age` variable, we print whether this person can drive or not.

```output{ lineNos=false }
You can't drive yet.
```

We can even skip `else` block if it's not necessary.

```python
age = 22
if age > 18:
    print("You can drive")
print("End of If Block")
```

**Output**
```output{ lineNos=false }
You can drive.
End of If Block
```

This `if..else` construct is useful for situations where we have either or kind of situation. However, if we have to decide between more options, we can also specify more conditions using `if..elif..else` construct.

```python
num = -2
if num > 0:
    print("It's a positive number")
elif num < 0:
    print("It's a negative number.")
else:
    print("It's zero")
```

In above example, we have total three different options.

```output{ lineNos=false }
It's a negative number.
```

If we have more than two choices, the order in which we specify these conditions do matter. Basically, this conditional block will execute the first block where the condition holds `True` even though there may be other blocks which may be `True`. Consider below example, in this case, the student has got 88 marks and we should ideally get a message saying "You've got A!". However, when we execute, it prints incorrect grade

```python
marks = 88
if marks < 35:
    print("Sorry, you've failed.")
elif marks > 35:
    print("You've got D grade.")
elif marks > 60:
    print("You've got C!")
elif marks > 75:
    print("Nice! You've got B grade.")
else: 
    print("Congratulations, You've got A!")
```

**Output**
```output{ lineNos=false }
You've got D grade.
```

In order to fix this, we have to reshuffle the order in which the conditions are specified as shown below.

```python
marks = 88
if marks < 35:
    print("Sorry, you've failed.")
elif marks > 85:
    print("Congratulations, You've got A!")
elif marks > 75:
    print("Nice! You've got B grade.")
elif marks > 70:
    print("You've got C!")
else: 
    print("You've got D grade.")
```

```output{ lineNos=false }
Congratulations, You've got A!
```

We can also nest these `if..else` statements and create complex conditional logic. Basically inside `if` or `else` block, we can have additional `if..else` conditional checks.

## Conditionals with `None`

In earlier lesson, we learned that `None` is not `0`, `False` or empty string. Let's test those out.

```python
none_value = None
empty_string = ""
false_value = False
zero_value = 0
print(f"none_value == empty_string: {none_value == empty_string}")
print(f"none_value == false_value: {none_value == false_value}")
print(f"none_value == zero_value: {none_value == zero_value}")
print(f"none_value == None: {none_value == None}")
print(f"none_value is None: {none_value is None}")
```

**Output**
```output{ lineNos=false }
none_value == empty_string: False
none_value == false_value: False
none_value == zero_value: False
none_value == None: True
none_value is None: True
```

As you can see from the output, `None` value can be compared with another `None` value will return `True` otherwise it will return `False`.

## Ternary operator

Python also provides Ternary operator which reads like a plain English and can be used to assign values to a variable.

```python
age = 17
is_adult = "Yes" if age > 18 else "No"
print(is_adult) # No
```

In above example, `is_adult` will be assigned `No` because `age` variable has value less than 18.

## Pass keyword

Whenever we create a new block using indentation, we have to fill that block. The block cannot be left empty. If we leave the block empty, it will give `SyntaxError`. There may be scenario where you have not decided on the implementation of the block of code. In such cases, we can use `pass` keyword to skip that block and Python interpreter will not give `SyntaxError` if we write `pass` keyword. This can be useful for even function implementations which you may want to fill in later. Below is the syntax for using this keyword.

```python
if 1 == 1:
    pass
```