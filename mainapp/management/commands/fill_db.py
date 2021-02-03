from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

import json, os

JSON_PATH = 'mainapp/fixtures/'

def load_from_json(filename):
    with open(os.path.join(JSON_PATH, filename + '.json'), 'r') as f:
        return json.load(f)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for cat in categories:
            new_cat = ProductCategory(**cat)
            new_cat.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for prod in products:
            cat_name = prod['category']
            _cat = ProductCategory.objects.get(name=cat_name)
            prod['category'] = _cat
            new_prod = Product(**prod)
            new_prod.save()

        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age='22')
