import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','practice2.settings')

import django
django.setup()

## fake pop scripts

import random

from user_app.models import User,AccessRecord
from faker import Faker

fakergen = Faker()

def populate(N = 5) :
    for entry  in range(N) :
        fake_name = fakergen.name()
        fake_last = fakergen.name()
        fake_email = fakergen.email()
        fake_date = fakergen.date()

        # create the new webpage entry

        user_list = User.objects.get_or_create(Name = fake_name,LastName = fake_last, Email  = fake_email )[0]

        # fake access reocrd

        accRcd = AccessRecord.objects.get_or_create(Name = user_list, date = fake_date)[0]


if __name__ == "__main__":
    print("populate script")
    populate(20)
    print("populate complete")
