import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','models_and_database.settings')

import django
django.setup()

## fake pop scripts

import random

from first_model.models import Topic,AccessRecord,Webpage
from faker import Faker

fakergen = Faker()

topics = ['social_websites','games','News','search','laptops']

def add_topics():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5) :
    for entry  in range(N) :
        # get topic name from the add_topics
        top = add_topics()
        #   create fake data for the entry

        fake_url = fakergen.url()
        fake_date = fakergen.date()
        fake_name = fakergen.company()

        # create the new webpage entry

        webpage = Webpage.objects.get_or_create(category = top,url = fake_url, Name  = fake_name )[0]

        # fake access reocrd

        accRcd = AccessRecord.objects.get_or_create(Name = webpage, date = fake_date)[0]


if __name__ == "__main__":
    print("populate script")
    populate(20)
    print("populate complete")
