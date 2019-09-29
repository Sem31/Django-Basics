import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Models_pro.settings')

import django
django.setup()

#fake pop script
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen  = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def population(N=5):

    for entry in range(N):

        #get topic
        top = add_topic()

        #get fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the webpage
        webpg = Webpage.objects.get_or_create(topic = top,url = fake_url,name = fake_name)[0]

        #fake accessrecords
        acc_rec  = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)


if __name__ == "__main__":
    print('Populate the script')
    population(20)
    print('Populatating complete')