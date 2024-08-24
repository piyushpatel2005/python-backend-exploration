# Overview of Python

In this lesson, we will see what is Python and how to set up local development environment to learn Python.

## History of Python

Python was developed in 1990 and it is now one of the most popular general-purpose languages available. This means it can be used for pretty much anything. 
Python has had few major rleases. Python 2.7 was widely used for a long time. However, Python Foundation decided to deprecate this version in 2020. Now, the latest major version is Python 3 and it comes with newer versions of the UNIX systems. We will learn only Python 3.

Let's take a look at some of the features of Python.

## Why learn Python?
Below are some of features of Python programming language

1. Very concise and readable. Python code tends to be very readable compared to other languages. They do not require curly braces or semi-colon at the end of each statements.
2. Dynamic Programming language: This means you do not need to specify the data type with each variable and function declaration. This reduces code verbosity.
3. Open source: This means anyone can read the actual code and fix bugs. This means there are lots of contributors and less probability of code bugs. 
4. Cross-platform: This means the code written in one operating system can still work on another operating system.
5. Interpreted language: This means during execution time, each line is interpreted to the machine language one line at a time. Other languages like C++, Java, C# are compiled languages which means they are first compiled into machine code and during execution they only use those machine code. With Python, this extra compilation step is skipped.
6. Memory management and Garbage collection: Python has built-in support for Garbage collection. That means we don't have to worry about allocating and then deallocating memory from our system. Python interpreter will take care of this.
7. Packages and Dependency management: It comes with `pip` which is a tool used to manage dependencies. It also has wide community of developers who have themselves developed lots of general computing packages. That means anything you want to do, most likely someone has written code for that and you can simply reuse their code by importing their packages.

## Where Python is Used?

Now, let's talk about where Python language is being used. Python is used for multiple different applicationsthis includes following:

- Web development
- Machine Learning and AI
- Image Processing
- Game development
- GUI development
- Networking and System development
- Automation


### Who is using Python

Some of the biggest enterprises are using Python this includes Google, Facebook, Microsoft, Twitter and many more. Most of the companies that are into data science are leveraging some of the packages available with Python. Python is a vast community of data scientist and data analyst and that's why it has wide support for machine learning DNA applicationsread it

## How to set up Local Development Environment

In order to write code in Python, all we need is Python development kit which includes Python interpreter. Just browse to [Python official website Downloads section](https://www.python.org/downloads/). According to your operating system, it will suggest to download specific installer at the top with **Download Python** button. Click that button and it will download the installer. According to your operating system, install that executable file. Once installed, you can verify the Python installation by using following.

```shell{ .show-prompt lineNos=false }
python -V
```

This command should show the installed version of Python. That's it and we can start learning Python.

## Hello World in Python

Let's also take a look at how to execute Python programs. In the below code, I have written the conventional "Hello World" code in Python.

Create a new file in your workspace directory with name `hello.py` and add the content from below code.

```python
print("Hello World")
```

Now, to execute this code, you can either use Code Runner which comes with Visual Studio Code or on command prompt or terminal, navigate to your workspace directory and type below command.

```shell{ .show-prompt lineNos=false }
python hello.py
```

```console{lineNos=false}
Hello World
```

This code is very simple in which we call built-in function called `print` which, as the name suggests, prints the arguments passed between parentheses. In this, we put `Hello World` so it printed the same in the output.

Let's add few more lines and print few more values.

```python
print("Hello World")
print(100)
print(99.99)
```

```shell
python hello.py
```

The output looks like below.

```console{lineNos=false}
Hello World
100
99.99
```