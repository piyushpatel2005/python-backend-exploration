# Object Oriented Programming - Classes and Objects

In this lesson, we introduce the concept of Object oriented programming in the context of Python as a programming language. We will learn about what classes are and how to use them to create different objects.

## What is Object-Oriented Programming (OOP)?

Object oriented programming is a programming style in many popular programming languages. From Wikipedia,

> Object-oriented programming (OOP) is a programming paradigm that organizes data and code into objects. Each object has a set of attributes (also known as properties or fields) and methods (also known as functions) that can be used to manipulate the object’s data.

Above definition clearly explains what is object oriented programming. When you're programming your system, the code size may be very large in terms of thousands of lines of code. We can certainly use modules and packages to divide the code but Object oriented programming provides another level of code modularity. We can create self-contained objects which can have properties and methods. A class will have data attribute and behaviors using methods. Properties are used to store some form of information. For example, a human can have 2 eyes, 2 hands and 2 legs. Methods, on the other hand, are the actions an object can perform. For example, humans can walk, eat and sing. Of course, humans can have many other attributes and can do many other things but these are just a simple example. We include only relevant information in our objects.

OOP Programming style provides several benefits:
1. Inheritance
2. Polymorphism
3. Abstraction
4. Encapsulation

## Defining Classes

Classes are blueprints of objects. Once we have a class defined, we can create many different independent objects of the same type. All objects may have similar attributes but all of them may have different values assigned to them. So, in order to create an object, we first have to define the class for it. A class is defined using the keyword `class` in Python. For example, below code defines a class `Person`. 

```python
class Person:
    pass
```

## Creating Objects from a Class

This class is almost useless except that it is still a valid class. It does not have any properties nor does it have any methods. Now, that we have class defined, we can create objects from this class using the class name followed by pair of parenthesis. Creating an object is also called instantiating an object or instance of a class.

```python
person1 = Person()
person2 = Person()
```

### Everything is an object

In fact, in Python, everything is an object. This means everything has values and methods associated with them. To see the available attributes we can use `dir()` function.

```python
str = 'Hello'
print(dir(str))
```

**Output:**

```output{ lineNos=false }
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

## Constructor of a class

This lists all the available methods on string object `Hello`. The methods that start with `__` are not supposed to be called directly. They are used internally when we perform certain operations on this object. Here, you can see some of the methods we have already used like `find`, `index`, `split`, etc.

Now, our class `Person` is not interesting because it cannot do anything. So, let's see how we can add data (attributes) and methods (functionalities) to it.

**Example:**

```python
class Person:
    def __init__(self):
        self.name = "Daniel"
        self.age = 28
        self.nationality = "American"
person = Person()
print(person.name, person.age, person.nationality)
```

In this code, I have defined `Person` class again but this time, I have defined a method `__init__()` inside the class definition. Note the indentation of this method. It is part of `Person` class definition. This method is special method like every other method starting with double underscores (`__`). This method is called constructor of the class. This is executed everytime we create an object of `Person` class. Every method defined inside a class will always have `self` as the first parameter and when calling these methods, we do not need to pass this as an argument. Inside, this method, we have `self.name`, `self.age` and `self.nationality`. These are called properties of an object. In this case, we have defined a person whose `name` is 'Daniel' with `age` 28 years. When defining attributes of an object, we use `self` keyword and when retrieving these data values, we use the object name which in this case is `person` from line `6`.

**Output:**

```output{lineNos=false }
Daniel 28 American
```

In above class, we have the data attributes with hard-coded values. So, if we create another instance fo the `Person` class and check their properties, they will have the same values which is non-interesting.

```python
person1 = Person()
person2 = Person()
print(person1.name) # Daniel
print(person2.name) # Daniel
```

## Class with Attributes and Methods

Let's see how we can have individual `Person` instances with their own attributes. Also, let's see how to add some methods to this class.

```python
class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
        
    def introduce(self):
        return f"{self.name} with {self.age}"

alex = Person("Alex", 30, "Canadian")
daniel = Person("Daniel", 28, "American")

print(alex.introduce())
print(daniel.introduce())
```

This `Person` class has different `__init__()` method. Here, we are having four parameters. First one is `self` and then 3 other parameters. When instantiating an object of this class, we have to pass three arguments as shown in line `10` and `11`. These values get passed into `self.name`, `self.age` and `self.nationality`. Above code has a method `introduce()` defined inside the class `Person`. Again, this method has first parameter of `self`. When calling the method, we do not have to pass argument for this as can be seen on line `13` and `14`.

**Output:**

```output{ lineNos=false }
Alex with 30
Daniel with 28
```