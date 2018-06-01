import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

import random 
from second_app.models import User
from faker import Faker

fake = Faker()

def user():
    first_name = fake.first_name() 
    last_name = fake.last_name()
    email = fake.email()
    user =  User.objects.get_or_create(first_name=first_name, last_name=last_name, email= email)[0]
    user.save()
    return user

def populate_users(n=5):
    for u in range (n):
        user()
        

if __name__=='__main__':
    print("populating script")
    populate_users(20)
    print("populating complete")
