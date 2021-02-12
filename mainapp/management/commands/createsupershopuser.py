from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from sys import argv

name = str(argv[2])
email = str(argv[3])
password = str(argv[4])
age = int(argv[5])

class Command(BaseCommand):
    if all([name, email, password, age]):
        ShopUser.objects.create_superuser(name, email, password, age=age)
