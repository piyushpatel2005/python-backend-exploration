---
title: Introduction to FastAPI
---

# Introduction to FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. FastAPI is mainly for developing high performance web APIs and is built on top of Starlette for the web parts and Pydantic for the data parts. That doesn't mean you cannot use it for traditional web apps. You can still use FastAPI for traditional web applications, but it's more suitable for APIs.

FastAPI was announced by Sebastian Ramirez in 2018 and has since gained a lot of popularity due to its speed and ease of use. It is one of the fastest web frameworks available for Python. FastAPI is built on top of Starlette for the web parts and Pydantic for the data parts. It is designed to be easy to use and learn, and it is also very fast.

## Intro to Async Processing in Python

Python added asynchronous processing support in Python 3.5+ versions. In async applications, only single thread runs, but it can switch between tasks. For example, if our application makes call to another function in external API, when we send request, we are just waiting for response from the other api endpoint. This wait-time CPU cycles could be utilized to perform some other tasks. So, CPU can take on other tasks during the time it's waiting for response from other API. When we receive a response from the API, the original function can continue doing its further processing. This way we are utilizing compute resources more efficiently. FastAPI is designed to work with `async` and `await` keywords in Python. It is fully asynchronous and supports both synchronous and asynchronous code.

In an asynchronous application, the processing logic is encapsulated in coroutines instead of traditional Python functions. Coroutines are functions that can pause and resume their execution. They are defined using the `async def` syntax. The `await` keyword is used to pause the execution of a coroutine until the result is available. 

Many Python web frameworks were developed before the introduction of asynchrounous processing in Python. They were implementing WSGI (Web server Gateway Interface) specs. To leverage these new features, new specifications ASGI (Asynchronous Server Gateway Interface) was introduced. ASGI is designed to work with `async` and `await` keywords in Python. [Starlette](https://pypi.org/project/starlette/) is an ASGI framework and FastAPI is built on top of Starlette. In order to serve applications, we need a web server with ASGI support. [Uvicorn](https://pypi.org/project/unicorn/) is a lightning-fast ASGI server implementation.

## Features of FastAPI

- **Fast**: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). It is one of the fastest web frameworks available in Python.
- **Faster Development**: FastAPI can increase developer productivity as it comes built in with many features that are common in web development.
- **Fewer bugs**: It includes type hinting and models to help reduce bugs in your code.
- **Intuitive**: It has greate code editor support in most popular IDEs.
- **Robust**: Get production-ready code. With automatic interactive documentation.
- **Standards-based**: Based on standard Python type hints. It is fully type hinted. Even the parameters and return types are type hinted.
- **Fully asynchronous**: Supports both synchronous code and asynchronous code, and is designed to be easy to use in both cases.
- **Automatic interactive API documentation**: It provides auto-generated documentation and test pages out of box.
- **Dependency Injection**: Dependency injection system, that is easy to use, fast, and with no magic. You can use it to organize your code in a clean way.
- **Security**: Includes security utilities to authenticate requests, including OAuth2, API keys, and more.
- **Testable**: It provides relatively easy structure to write tests for your code.

## Who uses FastAPI?

FastAPI is used by many companies and organizations. Some of the companies that use FastAPI are:

- Microsoft
- Netflix
- Uber
- LinkedIn
- Walmart

## Intro to RESTful APIs

REST stands for Representational State Transfer. It is a software architectural style for designing networked applications that defines how an application should behave. REST is a resource-based architecture rather than action based as is the case in RPC or SOAP. Everything on a RESTful API is a resource and can be accessed using standard HTTP methods. RESTful APIs are stateless, meaning that each request is independent of the others. RESTful APIs are designed to be simple and easy to use, which makes them a popular choice for developers. It provides uniform interfaces for interacting with resources. RESTful APIs are designed to be scalable and flexible, making them a good choice for building web services.

### HTTP Methods
RESTful APIs are built on top of HTTP. HTTP (Hypertext Transfer Protocol) is a protocol that allows the fetching of resources, such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser. HTTP protocol includes several methods that are used to interact with resources. The most common methods are `GET`, `POST`, `PUT`, `DELETE`, and `PATCH`. These methods are used to perform different operations on resources. RESTful APIs use these methods to interact with resources. Below list outlines brief information on each of these methods.

 - **GET**: The `GET` method requests a representation of the specified resource. Requests using `GET` should only retrieve data. This is the most widely used method in HTTP.
- **POST**: The `POST` method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server. This is not an idempotent operation. That is invoking the same request multiple times will have different results.
- **PUT**: The `PUT` method replaces all current representations of the target resource with the request payload. If we have a user with id 1 and we send a PUT request with a new user object, the full content of this user gets replaced.
- **DELETE**: The DELETE method deletes the specified resource. 
- **PATCH**: The PATCH method is used to apply partial modifications to a resource.