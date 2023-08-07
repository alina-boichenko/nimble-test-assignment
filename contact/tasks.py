from celery import shared_task
import os
import requests

from contact.models import User

CONTACTS_NIMBLE_API = "https://api.nimble.com/api/v1/contacts"
SLEEP_TIME = 86400
NIMBLE_API_KEY = os.getenv("KEY_NIMBLE_API")
HEADERS = {"Authorization": f"Bearer {NIMBLE_API_KEY}"}


def get_pages_count() -> int:
    response = requests.get(url=CONTACTS_NIMBLE_API, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        pages = data["meta"]["pages"]
        return pages


@shared_task
def update_contacts() -> None:
    pages = get_pages_count()

    for page in range(1, pages + 1):
        params = {"page": page}
        response = requests.get(url=CONTACTS_NIMBLE_API, headers=HEADERS, params=params)
        data = response.json()

        for row in data.get("resources"):
            if row.get("record_type") == "person":
                first_name = row.get("fields").get("first name")[0].get("value")
                last_name = row.get("fields").get("last name")[0].get("value")
                email = row.get("fields").get("email")
                if email:
                    email = email[0].get("value")

                User.objects.create(
                    first_name=first_name, last_name=last_name, email=email
                )


@shared_task
def daily_update_contacts():
    update_contacts.delay()
