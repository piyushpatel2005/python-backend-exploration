# Variable Scopes in Python

Variables scope defines where the variable is accessible in the program. We can think of this as the lifetime of a variable. Outside this scope, the variable no longer exist.

Variable scope represents the duration of the code where the variable exists. Python removes unnecessary variables when we no longer need them in order to save memory in our system. This process is sometimes called *garbage collection*.

## Local Variable Scope

All the variables defined inside the body of a function are called **local variables**.

```python
def sample_fn():
    name = "Jessica" # we cannot use this outside the function body
    print(name)

sample_fn()
print(name)
```

This produces an error because local variable `name` is not available outside the `sample_fn` function on line 6.

```console{ lineNos=false }
$ python main.py
Jessica
NameError: name 'name' is not defined
```

## Global Scope Variable

**Global variables** are variables defined outside any function body and they are available anywhere in the code. 

```python
name = "Andrew" # global variable

def sample_fn():
    name = "Jessica" # Local variable: we cannot use this outside the function body
    print(name)

sample_fn()
print(name)
```

In this case, because we have defined `name` variable outside any function at the top level. This is called Global variable and this is accessible anywhere in the program even at line 8 outside the `sample_fn` function.

**Output:**
```output{ lineNos=false }
Jessica
Andrew
```

We can also access the global variables inside the function. If we modify the global variable after using `global` keyword, it will actually modify the variable value even outside the function body.

```python
name = "Andrew" # global variable

def sample_fn():
    global name
    name = "Jessica"
    print(name)

sample_fn()
print(name)
```

This code block modifies global `name` variable and hence this prints the same name two times.

**Output:**
```output{ lineNos=false }
Jessica
Jessica
```

{{< admonition tip >}}
We should avoid modifying global variables inside a function to avoid confusion. This can result in bugs which can be difficult to trace.
{{< /admonition >}}

## Block Level Variables

Python doesn't have block level scope. In other languages, the variable defined inside the block is not accessible outside the code block. However, in below example, the variable defined on line 3 is surprisingly accessible on line 5 and similarly for variable inside `while` block is also accessible outside it.

```python
def sample_fun():
    if True:
        result = "Block variable"
    # Outside if block
    print(result)
    
    i = 0
    while i < 1:
        i += 1
        another_result = "Another block variable"
    # Outside while block
    print(another_result)

sample_fun()
```

**Output:**
```output{ lineNos=false }
Block variable
Another block variable
```