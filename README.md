## Installing Python, Postgres, Django
- check if python installed
  > $ python3 --version
  > $ pip3 --version
- install python and pip if not 
  > $ sudo apt install python3
  > $ sudo apt install python3-pip
- install postgres (easiest to install app from online) - https://www.postgresql.org/download/

## Cloning repo and virtual environment
- git clone
- cd into directory
- install venv module if not installed yet (it's most likely installed)
  > $ sudo apt install python3-venv
- create and enter a new virtual environment 
  > $ python3 -m venv venv (can name it whatever you want, I named mine venv)\
  > $ source venv/bin/activate (enter the new environment)\
  > $ pip install -r requirements.txt\

## Create Database and configure /crm/crm/settings.py
- create database - I named mine crm
- create superuser for server in pgadmin4 - right click login/group roles, add user, password, and toggle superuser privilege
- enter this username and pw in the settings.py file
- for future reference when tables are made - do:
  > python manage.py makemigrations\
  > python manage.py migrate
- fill in other empty variables in settings.py, including secret key (search how to generate django secret key)

## To run the project
- cd into crm directory
  > $ python3 manage.py runserver
