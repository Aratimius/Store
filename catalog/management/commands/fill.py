import json
from catalog.models import Product, Category
from django.core.management import BaseCommand


class Command(BaseCommand):
    @staticmethod
    def json_read_data():
        with open('data.json') as json_file:
            data = json.load(json_file)
        return data

    def handle(self, *args, **options):
        Product.objects.all().delete
        Category.objects.all().delete

        products_for_create = []
        categories_for_create = []

        for item in Command.json_read_data():
            if item['model'] == 'catalog.category':
                categories_for_create.append(
                    Category(pk=item['pk'], name=item['fields']['name'], description=item['fields']['description'])
                )
        Category.objects.bulk_create(categories_for_create)

        for item in Command.json_read_data():
            if item['model'] == 'catalog.product':
                products_for_create.append(
                    Product(pk=item['pk'], name=item['fields']['name'], description=item['fields']['description'],
                            preview=item['fields']['preview'], category=Category.objects.get(pk=item['fields']['category']),
                            price=item['fields']['price'], created_at=item['fields']['created_at'],
                            updated_at=item['fields']['updated_at'])
                )
        Product.objects.bulk_create(products_for_create)
