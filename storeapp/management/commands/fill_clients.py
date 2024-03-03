import datetime
from django.core.management.base import BaseCommand
from store_app.models import Client
from random import randint


class Command(BaseCommand):
    help = 'Fill clients'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(count):
            client = Client(
                name=f'Client {i}',
                email=f'client{i}@example.com',
                phone_number=f'8-990-456-98-{randint(0, 9)}{randint(0, 9)}',
                address=f'Address {i}',
                registration_date=datetime.date(2024, 1, 5),
            )
            client.save()
        self.stdout.write(str(f'{count} created clients'))

