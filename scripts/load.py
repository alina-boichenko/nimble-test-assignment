import csv

from contact.models import User


def run():
    with open("nimble_contacts.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            User.objects.create(first_name=row[0], last_name=row[1], email=row[2])
