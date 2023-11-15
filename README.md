# Tutorial: Getting Started with Django
### Introduction
Welcome to our tutorial on building a Django backend with a database. In this tutorial, we'll cover the basics of Django, migrations, models, factories, seeding the database with fake data, and testing the database. This step-by-step guide will help other users in developing a solid foundation using Django. 

### Authors
- Chiara daSilva Santos
- Christian Wantong
- Michael Daniels

### Prerequisites
Ensure that you have the following installed on your system
- Python
- Pip (Python Package Installer)
- Django

To install Django, run the following command on terminal:
pip install django


#### Step 1: Setting up the Project
1. Create a Django Project:
django-admin startproject myproject

2. Navigate to Your Project:
cd my project

#### Step 2: Creating Migrations and Models
1. Create a Django App: python manage.py startapp myapp
(you may need to change python to python3 depending on the version you are using)

2. Define a Model: