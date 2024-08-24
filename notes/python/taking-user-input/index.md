# Taking User Input

This lesson shows a simple function to take user input for console applications. Console application are also known as command-line application. Python has a function `input` which can be used to take user input.

## User input with built-in function

When interacting with user, we may need to take user responses for certain variables and based on user inputs, we may respond differently. For example, in an application which calculates student grades, we may have to ask for student marks for each subject and based on those, we can assign some grades or calculate average or GPA.

Python provides a function `input` which can be used to take user input. As per [official documentation for this function], this function takes an argument of prompt and waits for user input until user enters something with new line. Basic usage looks like this. Here, whatever user enters will be stored in `s` variable in the form of string data type.

```python
s = input("Enter something: ")
```

Let's see a simple example asking for user's name and then greeting them.

```python
name = input("Enter your name: ")
print(f"Hello {name}")
```

Execute this code and the console will wait for your input after prompt `Enter your name: `.

```shell{ .show-prompt lineNos=false }
python main.py
```

```output { lineNos=false}
Enter your name: Johny
Hello Johny
```

On caveat with `input` function is that it always returns `str` as output data type. That is ther variable being assigned will have value as string. If we want to take input as numerical value, then we will have to cast to required data type.

### Type Casting

Type casting is converting variable of one type into another. In Python, it's relatively straight forward. We just use the function for the data type to which we want to convert current value. Below code shows demo of type casting.

```python
i = 10 # int
decimal = 10.20 # float
int_to_str = str(i) # convert to str
float_to_int = int(decimal) # convert float to int
float_to_str = str(decimal) # convert float to str
int_to_float = float(i) # convert int to float
print(type(int_to_str)) # str
print(type(float_to_str)) # str
print(type(int_to_float)) # float
print(type(float_to_int)) # int
```

```output{ lineNos=false}
<class 'str'>
<class 'str'>
<class 'float'>
<class 'int'>
```

### How to take integer input from user?

Let's get back to `input` function and see what happens when we want to take `int` input.

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
age = age + 1
print(f"Hello {name}, next year you'll be {age} years old.")
```

```shell{ .show-prompt lineNos=false }
python main.py
Enter your name: John
Enter your age: 21
```
When executed, we get below error.

```output{ lineNos=false }
TypeError: can only concatenate str (not "int") to str
```

Here, when we try to input `age`. It takes 21 as `age` variable. However, this value is of type `str` and on next line, when we try to add `1` to this variable. It fails to understand that we are trying to perform addition. Python interpreter thinks we are trying to perform string concatenation (joining two strings). It cannot join `str` with `int` and hence throws `TypeError`. To fix this, we have to first cast `age` to `int` type.

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
age = age + 1
print(f"Hello {name}, next year you'll be {age} years old.")
```

```output{ lineNos=false }
Hello John, next year you'll be 22 years old.
```

## Conclusion

This lesson shows how you can take user input in command-line applications. We also saw how we have to explicitly cast from string data type to respective data type if we want input of type other than string.