# PortfolioProject
Django Tutorial Project

Overview

This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

The main features that have currently been implemented are:

There are models for books, book copies, genre, language and authors.
Users can view list and detail information for books and authors.
Admin users can create and manage models. The admin has been optimised (the basic registration is present in admin.py, but commented out).
Librarians can renew reserved books
Local Library Model

![](https://github.com/antonybest/PortfolioProject/blob/master/local_library_model_diagram.png)

Quick Start guide!

To get this project up and running locally on your computer:

Set up the Python development environment. It's recommended to use a Python virtual environment.

Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):

Cd myproject :- CHANGES INTO <your project> folder

Python3 –m venv venv : - CREATES A VIRTUAL ENVIRONMENT for your project

Source venv/bin/activate :- ACTIVATES THE VIRTUAL ENVIRONMENT

pip freeze # views requirements to be created (best done in virtual env)

pip freeze > requirements.txt # create requirements.txt (best done in virtual env)

ADD PACKAGE (EXAMPLE): - django== ‘version’ & pip == ‘version’ WITHIN THE REQUIREMENTS.TXT FILE (I like to do it this way, because you then have your packages in a clear & neat way

pip install -r requirements.txt # install requirements.txt (best done in virtual env, THIS THEN INSTALLS YOUR PACKAGES YOU WROTE IN THE REQUIREMENTS.TXT FILE)

django-admin startproject mysite : - CREATES THE MAIN HUB FOLDER OF THE WHOLE PROJECT I.E THE ADMIN PART OF YOUR SITE

Python3 manage.py runserver : - runs the server (VERY IMPORTANT BEFORE YOU START BUILDING, You know you project is working befroe you start :) )

python3 manage.py startapp catalog 

python3 manage.py makemigrations (After you have created your models in models.py)

python3 manage.py migrate (Moves the models to your database)

python3 manage.py createsuperuser # Create a superuser (This is so you can login to the admin part of your site http://127.0.0.1:8000/admin/)

python3 manage.py collectstatic

python3 manage.py test # Run the standard tests. These should all pass.

python3 manage.py runserver

Open a browser to http://127.0.0.1:8000/admin/ to open the admin site

Create a few test objects of each type.

Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.
