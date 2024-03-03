from django.core.management.base import BaseCommand
from ...models import Products
from random import randint


class Command(BaseCommand):
    help = 'Creates product'

    def handle(self, *args, **kwargs):
        for i in range(20):
            product = Products(
                name=f'Product {i}',
                description=f'Description {i}',
                price=randint(1, 1000),
                quantity=randint(1, 10),
                date_added=f'2024-01-{randint(0, 2)}{randint(1, 9)}',
            )
            product.save()
        self.stdout.write(str(f'{i} created products'))