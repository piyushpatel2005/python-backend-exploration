# Create First Django Project

When working on Django projects, it's ideal to use virtual environments. You can create a virtual environment using the following command.

```bash
python3 -m venv venv
```

It's best to omit this virtual environment from the source code repository. So, add this to your `.gitignore` file.

```bash
echo "venv" >> .gitignore
```

Once you've created your virtual environment, you can activate it.

```bash
source venv/bin/activate
```

## Install Django

Django comes as a Python module and can be installed using `pip` command. 

```bash
python -m pip install django
```

You can also verify the Django version using `python -m django --version` command. This tutorials are written using Django version 5.1.4.

Once you have Django installed, you can use the `django-admin` command to create a Django project.

## Creating Django Project

```bash
django-admin startproject firstproject
```

This creates a Python Django project structure with several Python module files and directories. 

```plaintext
firstproject/
    manage.py
    firstproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
```

This project directory includes `manage.py` file and also includes another directory with the same name as the project.

## Overview of Project Structure
This section covers basic information about the scripts and directories in a simple Django project.

### `manage.py`

The `manage.py` module can perform everything that `django-admin` utility can do. The general usage of the `manage.py` file is as follows.

```bash
python manage.py <command>
```

Below are some of the common commands that can be used with the `manage.py` file.

- **startapp**: Django project consists of multiple apps. You can create a new app using the `python manage.py startapp <app_name>` command.
- **runserver**: Django comes with a built-in web server which can be used to run the Django project. You can start the web server using the `python manage.py runserver` command.
- **createsuperuser**: You can create a superuser using the `python manage.py createsuperuser` command. This user can be used for managing the Django project using admin UI.
- **makemigrations**: Django manages the database changges using ORM technique. Migrations are database table who structure matches the data model declared in the app. You need to make migrations when a new model is created or updated.
- **migrate**: This command is used to apply the migrations. This basically synchronizes the database state with the models defined in the app.
- **shell**: This command starts a Python shell with Django project settings loaded. This is used to perform interactive operations or validating operations interactively.

### `settings.py`

Django comes with default `settings.py` which has default values for some configurations. If you want to modify the default values, you can modify the `settings.py` file. This file includes information about backend database, authentication, static files and other configurations.

### `urls.py`

This module includes all the URL mappings for the Django project. This is used to map URLs to views. The views are Python functions that handle the request and return the response to the client.

### `wsgi.py` and `asgi.py`

These files are used by the web server to run the Django project. The `wsgi.py` is used for WSGI (Web Server Gateway Interface) and `asgi.py` is used for ASGI (Application Server Gateway Interface).

## Running Your Application

You can test run your first Django project by using below command.

```bash
python manage.py runserver
```

This will start the development server on port 8000. If you want to change the port number, you can use the `--port` option. Visit `http://localhost:8000` to view the Django project. This will show simple Django project home page demonstrating successful installation of Django.