from django.core.management.base import BaseCommand
from store_app.models import Client


class Command(BaseCommand):
    help = 'Deletes client by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client} deleted')
        client.delete()
