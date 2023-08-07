# Nimble test assignment

## Setting environment variables
Create an empty file .env in the following path: nimble_test_assignment/.env Copy the entire content of the .env.sample file and paste it into the .env file. Modify the placeholders in the .env file with the actual environment variables. For example (but don`t use "< >" in your project):
``NIMBLE_API_KEY=NIMBLE_API_KEY``
## Installation:
Python3, Django REST, PostgreSQL, Celery, Redis must be already installed
```
git clone https://github.com/alina-boichenko/nimble-test-assignment.git
cd nimble_test_assignment
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirement.txt
python manage.py migrate
python manage.py runserver 
```

## Task 1. 
For import data from nimble_contacts.csv you need to use the following command in the terminal:
```
python3 manage.py runscript scripts.load
```
## Task 2
To update contacts from API https://api.nimble.com/api/v1/contacts you need to do next steps:
* Check if the server is running, if not: ``python manage.py runserver 
``
* Open a new terminal window and run Redis: ``redis-server``
* On the next new terminal run Celery: `` celery -A project worker -l info
``
* Open python console and input:
```
from contact.tasks import daily_update_contacts
daily_update_contacts()
```

## Task 3
This API http://127.0.0.1:8000/api/schema/swagger/ implements an endpoint with the contacts list and the ability to filter the results.
