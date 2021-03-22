from django.core.management.base import BaseCommand, CommandError
from authapp.models import ShopUser

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        new_user = ShopUser(email='aa@bb.ru', is_active=True)
        new_user.save()
        print('user added')