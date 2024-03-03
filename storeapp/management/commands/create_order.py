from django.core.management.base import BaseCommand
from ...models import Products, Order, Client
from random import choice


class Command(BaseCommand):
    help = 'Creates order'

    def handle(self, *args, **kwargs):

        clients = Client.objects.values_list('id', flat=True)
        client_id = choice(clients)
        product_id_list = Products.objects.values_list('id', flat=True)
        print(product_id_list)
        total_sum = 0
        products = []
        # for product_id in product_id_list:
        #     product = Products.objects.filter(pk=product_id).first()
        for i in range(5):
            product = Products.objects.filter(pk=choice(product_id_list)).first()
            products.append(product)
            total_sum += product.price
        client = Client.objects.filter(pk=client_id).first()
        order = Order(
            client=client,
            total_sum=total_sum,
        )
        order.save()
        for product in products:
            order.product.add(product)

        self.stdout.write(f'{order}')





