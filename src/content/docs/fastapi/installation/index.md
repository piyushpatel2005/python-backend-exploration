---
title: Installation for FastAPI Development
---

# FastAPI Environment Set up

In order to work with FastAPI, you need to have Python installed on your system. You can download Python from the official website [Python.org](https://www.python.org/downloads/).

In practice, when working with Python, it is recommended to use a virtual environment. A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. When you work on any Python projects, you will usually need to install other packages and it can be very difficult to manage all the dependencies. A virtual environment helps you to manage all the dependencies for your project. Python uses `pip` to manage dependencies.

## Setup FastAPI Environment

In this tutorials, I'm going to use Python version 3.9.11. So, you will have module `venv` available in Python 3.9. You can create a virtual environment using this module directly instead of relying on external package

```bash
python3 -m venv fastapi-env
```

Next, you can activate the virtual environment using the following command on Mac and Linux:

```bash
source fastapi-env/bin/activate
```

For Windows, you can use the following command:

```powershell
fastapi-env\Scripts\activate
```
### Installing FastAPI

Once this environment is activated, you can start installing the required packages. You can install FastAPI using the following command.

```bash
pip install fastapi
```

FastAPI will provide some built-in mechanisms which will make it easier to write web application code. A framework's job is to provide a structure for your code and make it easier to write and maintain. 

### Installing Uvicorn

You can also install `uvicorn[standard]` which is a lightning-fast ASGI server implementation, using the following command.

```bash
pip install uvicorn[standard]
```

As mentioned in the previous lesson, Uvicorn is an ASGI implementation for Python. To start the uvicorn server, you can run command `uvicorn main:app --reload`. By default, Uvicorn runs on port 8000. If needed, these parameters can be changed. Below command will start the server on port 8080.
 
```bash
uvicorn main:app --port 8080 --reload
```



Now, you can check the installed packages using `pip freeze` or `pip list` command. The good thing about using a virtual environment is that you can export the list of installed packages to a file `requirements.txt` and use it later to install the same packages in another environment. You don't have to check in these packages in your source code repository.

In order to deactivate the virtual environment, you can use one of the following commands based on your operating system.

```bash
deactivate  # On Mac and Linux
```

```powershell
fastapi-env\Scripts\deactivate
```

Going forward, always remember to activate your project's virtual environment before working on your project.