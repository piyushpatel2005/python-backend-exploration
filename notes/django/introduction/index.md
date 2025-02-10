# Introduction to Django

Django is one of the most popular web frameworks for Python. It is also one of the most feature-rich web framework. It is a high-level web framework that encourages rapid development and clean, pragmatic design. Django is a free and open-source web framework, written in Python, which follows the model-view-template architectural pattern.

## Prerequisites

Before you continue with this tutorial, it is expected that you know some Python programming. You should also have basic undestanding of HTML, CSS and Javascript although I will not be using much Javascript in this tutorial. You should also have code editor installed in your system which can be used to write Python, HTML, CSS and Javascript code. Something like VSCode, Atom or Sublime Text can work fine.

## History of Django

Django was created for writing newspaper articles at The Lawrence Journal-World. It was then converted into a web framework and released in 2005. It is now used by many organizations including some of the biggest fintech companies including Netflix, PayPal, Facebook, Dropbox and Stripe.

## Features of Django

Django is a high-level web framework that encourages rapid development and clean, pragmatic design. 
- It is free and open-source web framework, written in Python, which follows convention over configuration. 
- Django also provides built in commandline tool `django-admin` in order to manage your Django applications. 
- Django also comes with templating language called `Django template`. This is useful because you don't want to write the same HTML in multiple web pages. You can use template to write common HTML content in one file and import that file in multiple web pages and thus avoiding duplication of code. It also provides common programming constructs like `if..else` and `for` loops if you have to write similar content for multiple items in the web page.
- Django comes with a built-in authentication system which is very useful if you want to create a web application where you want to restrict access to certain pages or features based on the user's login status.
- It also comes in built-in ORM (Object Relational Mapper) which is very useful if you want to create a web application where you want to store data in a database. With the ORM, you can work with database in a simple way. You can invoke methods on the objects to create, read, update and delete data from the database without writing SQL statements.
- Django can be used to provide HTML response where the HTML content is built on the server side. It can also be used to write Restful APIs which can be useful when you want to expose your web application as a Restful API to either web or mobile clients.
- Django also comes with backend admin panel which is useful when you want to manage your database. You can use the admin panel to create, read, update and delete data from the database without writing SQL statements.
- Django has a rich community of developers who have written packages that are useful in many different applications. Also, the community can be helpful when you have a particular question about a feature of Django or if you're having some problem with the framework.
- It supports localization, multi-lingual support for complex web applications.

### Applications of Django

Django can be used to write complex web applications.

- It can be used to write common content management sites like blogs, news articles, forums, etc. It comes with backend for managing the content so this is straight forward use case.
- Django can be used to write e-commerce like web applications where you have a catalog of products. You can use ORM to manage product items and have users add items to their cart and checkout.
- Django can also be useful for writing backend APIs which can later be used for single-page applications.
- It can also be used for static web sites where the content is pre-generated and deployed to the web server. When user requests specific path, the server simply responds with HTML page which is pre-generated.
