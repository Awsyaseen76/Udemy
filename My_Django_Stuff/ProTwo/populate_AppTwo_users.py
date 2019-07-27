import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from AppTwo.models import Users
from faker import Faker

userGen = Faker()

def populate(n=5):
    for user in range(n):    
        fake_first = userGen.first_name()
        fake_last = userGen.last_name()
        fake_email = userGen.email()
        print('The Users Class')
        print(fake_email)
        
        Users.objects.get_or_create(first_name= fake_first, last_name=fake_last, email=fake_email)
        # usr.save()
    
if __name__ == "__main__":
    print('generate Users')
    populate(10)
    print('generation finished')