---
title: "Continue Break Statements"
date: 2023-08-04T05:04:11-04:00
draft: false
---

When using loops, sometimes we want to skip one of the execution in between depending on certain condition or we may want to stop further execution when certain condition meets on top of terminating condition. This is where `continue` and `break` statements come in handy.

<!--more-->

## Break Statement

In Python, `break` statement can be useful to break an iteration on specific condition. This can be useful for prematurely ending loops. For example, I am collecting user input and as soon as a user enters 'q' or 'quit', I want the code to exit otherwise continue prompting user for more input. In that case, we can make use of `break` statement. Break statement will break out the of the loop. Let's see how to implement that.

```python
while True:
    user_input = input("Can you guess the word?: ")
    if user_input == "q" or user_input == "quit":
        print("You guessed it right!")
        print("Good bye")
        break
    else:
        print("No, that's not what I thought. Guess again!")
```
In this code, we prompt user for guessing a word. If user enters anything other than `q` or `quit`, the code continues prompting the user. When user enter `quit`, the code exits.

**Output**
```output{ lineNos=false }
Can you guess the word?: someword
No, that's not what I thought. Guess again!
Can you guess the word?: somethingelse
No, that's not what I thought. Guess again!
Can you guess the word?: quit
You guessed it right!
Good bye
```

## Continue Statement

Similar to `break` statement, if we're writing a code and want to skip only few iterations of a loop, in those cases we can use `continue` statement to skip on certain condition using `if` clause. For example, in below code, I want to print all numbers up to 10, but I want to skip only `5` and `7`, then we can use for loop to print numbers. However, to skip `5` and `7`, we can use `continue` statement. It will skip that iteration and continue with the next one.

```python
for i in range(10):
    if i == 5 or i == 7:
        continue
    print(i)
```

**Output**

```output{ lineNos=false }
0
1
2
3
4
6
8
9
```
