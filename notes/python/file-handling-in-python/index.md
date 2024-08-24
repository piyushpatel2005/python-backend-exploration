# File Handling in Python

Python supports file handling just like any other programming language. File operations are usually performed at OS level but Python provides convenient methods and objects to interact with files. Python makes it really easy to operate with files.

## Overview

Working with files can be very tricky. There are three main steps to work with files.

1. Open a file
2. Work with the file
3. Close the file

While working with files, we first open the file. This provides a file handle. This is kind of pointer that keeps track of how many lines or characters you have read in a file. We can interact with files using this file handle. It provides methods to read contents of the file or we can write to file using different methods on this file handle. Finally, we need to make sure that we close the file. We should always make sure to close the file because they can consume unnecessary resources in your system. So, best practice is to always close the file.

## Opening a File in Python

For opening a file, we can use the `open` function in Python. Let's take an example of reading a file. Let's say I have sample file with two lines in it and the file name is `sample.txt` in the current directory.

```shell
cat sample.txt
```

```output{ lineNos=false }
This is sample text.
This is new line.
```

Now, to open this file, we can use below code.

```python
f = open('sample.txt')
```

In this case, the file is in the current directory, that's why it doesn't need full path. However, if the file was in different directory, it will require corresponding relative path or absolute path. If we try to open a file and provide incorrect path or the file does not exist with that name, we get `FileNotFoundError`.

**Example:**

```python
f = open("non-existing.txt")
```

**Output:**

```output{ lineNos=false }
FileNotFoundError: [Errno 2] No such file or directory: 'non-existing.txt'
```

Once, we get file handle `f`, we can check whether the file is closed or it is open. If the file is not closed, that is if it is open, we can close the file using `close()` method on file handle.

```python
f = open('sample.txt')
print(f.closed) # False
# close the file
f.close()
print(f.closed) # True
```

## Reading File Content

To read the contents of the file, we can use `read()` method to read specific number of bytes. We can pass a number, and we get back those many characters from the file.

**Example:**

```python
f = open('sample.txt')
text = f.read(3)
f.close()
print(text)
```

**Output:**

```output{ lineNos=false }
Thi
```

We can call multiple times to read further characters and we can reset back to specific position using `seek()` method.


```python
f = open('sample.txt')
print(f.read(3)) # 'Thi'
print(f.read(5)) # 's is '
f.seek(5)
print(f.read(10)) # 'is sample '
f.close()
```

This is quite difficult to keep track of. Python also provides a way to read complete file using `readlines()` method. This returns each line in the form the a `list`. We can also iterate over all the lines using `for` loop.

**Example:**

```python
f = open("data/test.txt")
for line in f.readlines():
    print(line)
f.close()
```

There is an extar new line due to `print()` function produces new line each time it runs.
**Output:**

```output{ lineNos=false }
This is sample text.

This is new line.
```

## Writing to a File

Now, let's understand how we can write to a file. Python provides consistent API for working with files. For writing files, we can use the same file handle which we can get using `open()` function. When opening a file using this function `open()`, we can provide `filemode` to open a file in write mode. We can find different options we can pass to `open()` function in its [documentation](https://docs.python.org/3/library/functions.html#open). For text files, we will focus on `w` and `a` mode. To open file for writing, we can specify second argument as `w`. By default, `open()` function opens in read mode which can be explicitly specified using character `r`. Below are the most commonly used modes for text files.

| Character | Meaning |
|:----------:|:-------|
| `r` | Read mode (default) |
| `w` | Write mode (overwrites existing files) |
| `a` | Append mode |

**Example:**

```python
f = open("test.txt", "w")
f.write("Hi\n")
f.close()
```

Above code snippet writes a file named `test.txt` with content `Hi` in it. However, if we try to modify the content and write again using write mode (`w`), it will overwrite the content.

To append to existing file, we can use append mode (`a`).

```python
f = open("test.txt", "a")
f.write("How are you?\n")
f.close()
```

We can also write multiple lines using `writelines()` method. This method takes a collection to write them just like `readlines()` method returns a collection.

**Example:**

```python
lines = ["This is sample text\n", "This is another sample\n"]
f = open("another.txt", "a")
f.writelines(lines)
f.close()
```

Python provides a convenient way to handle files. For working with files we have to open and close the file. It's so common that Python also provides another short hand syntax for working with files using `with` block. In this, we use `with` keyword to open context block where we open the file. Inside this context block, we have file handle available and can perform operations on the file. When we exit out of this block, the file will be automatically closed. We don't have to explicitly call `close()` method on the file handle. This is the preferred method for working with files.

```python
with open("sample.txt") as f:
    for line in f.readlines():
        print(line)
```