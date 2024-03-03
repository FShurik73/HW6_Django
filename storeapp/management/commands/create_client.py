from django.core.management.base import BaseCommand
from ...models import Client
from random import randint


class Command(BaseCommand):
    help = 'Creates client'

    def handle(self, *args, **kwargs):
        for i in range(10):
            client = Client(
                name=f'Client {i}',
                email=f'client{i}@example.com',
                phone_number=f'8-990-456-98-{randint(0, 9)}{randint(0, 9)}',
                address=f'Address {i}',
                registration_date=f'2024-01-{randint(0, 2)}{randint(1, 9)}',
            )
            client.save()

        self.stdout.write(str(f'{i} created clients'))