---
title: Introduction to Restful APIs
---

# Intro to RESTful APIs

REST stands for Representational State Transfer. It is a software architectural style for designing networked applications that defines how an application should behave.

## Intro to HTTP

Before diving into REST architecture, it's important to understand the HTTP protocol. 

HTTP stands for Hypertext Transfer Protocol. It is the foundation of any data exchange on the Web. It is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser. HTTP protocol includes several methods that are used to interact with resources. The most common methods are `GET`, `POST`, `PUT`, `DELETE`, and `PATCH`. These methods are used to perform different operations on resources. RESTful APIs use these methods to interact with resources.

### HTTP Methods

HTTP protocol includes several methods that are used to interact with resources. The most common methods are `GET`, `POST`, `PUT`, `DELETE`, and `PATCH`. 

- **GET**: The `GET` method requests a representation of the specified resource. Requests using `GET` should only retrieve data. This is the most widely used method in HTTP.
- **POST**: The `POST` method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server. This is not an idempotent operation. That is invoking the same request multiple times will have different results.
- **PUT**: The `PUT` method replaces all current representations of the target resource with the request payload. If we have a user with id 1 and we send a PUT request with a new user object, the full content of this user gets replaced.
- **DELETE**: The DELETE method deletes the specified resource.
- **PATCH**: The PATCH method is used to apply partial modifications to a resource.

These methods are used to perform different operations on resources. RESTful APIs use these methods to interact with resources. These operations are performed on resources and are abbreviated as CRUD operations (Create, Read, Update, Delete).

## What is an API?

API stands for Application Programming Interface. It is a set of rules and protocols that allow one software application to interact with another. APIs are used to define the methods and data formats that applications can use to communicate with each other. APIs are used to enable communication between different software systems.

In simple terms, the client and server agree on a set of rules for communication. The client sends a request to the server, and the server sends a response back to the client. APIs are used to define the methods and data formats that applications can use to communicate with each other.

## REST Architecture

RESTful APIs are built on top of HTTP. HTTP (Hypertext Transfer Protocol) is a protocol that allows the fetching of resources, such as HTML documents. It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser.

REST is a resource-based architecture rather than action based as is the case in RPC or SOAP. Everything on a RESTful API is a resource and can be accessed using standard HTTP methods. RESTful APIs are stateless, meaning that each request is independent of the others. RESTful APIs are designed to be simple and easy to use, which makes them a popular choice for developers. It provides uniform interfaces for interacting with resources. RESTful APIs are designed to be scalable and flexible, making them a good choice for building web services.

### RESTful API Principles

RESTful APIs have certain properties that they follow. These properties are known as the RESTful API principles.

1. **Stateless**: RESTful APIs are stateless, meaning that each request is independent of the others. The server does not store any information about the client session. Each request from the client must contain all the information needed to process the request.
2. **Client-Server Architecture**: RESTful APIs follow a client-server architecture. The client and server are separate entities that communicate over the network. The client is responsible for the user interface and the server is responsible for the data storage and processing.
3. **Uniform Interface**: RESTful APIs provide a uniform interface for interacting with resources. This means that all resources are accessed using standard HTTP methods, such as `GET`, `POST`, `PUT`, `DELETE`, and `PATCH`.
4. **Cacheable**: RESTful APIs are designed to be cacheable. This means that responses from the server can be cached by the client to improve performance.
5. **Layered System**: RESTful APIs are designed to be layered. This means that the client does not need to know the internal workings of the server. The client interacts with the server through a well-defined interface.
6. **Self-descriptive Messages**: RESTful APIs use self-descriptive messages. This means that each message contains all the information needed to process the request.