from datetime import datetime, timedelta
from .forms import ProductsForm
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponsePermanentRedirect
from .models import Client, Order, Products
import logging
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist


logger = logging.getLogger(__name__)


def index(request, product_id: int):
    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()
            logger.info(f' {product.name=}, {product.description=}, {product.price=}, {product.quantity=}, {product.image=}.')
            message = 'Товар успешно изменен'

            return render(request, "storeapp/index.html", {'form': form, 'message': message})

    else:
        form = ProductsForm()
        message = 'Заполните форму'
        return render(request, "storeapp/index.html", {'form': form, 'message': message})


def basket(request, client_id):
    products = []
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client).all()
    for order in orders:
        products.append(order.product.all())
    products.reverse()
    return render(request, 'storeapp/all_orders.html', {'client': client, 'orders': orders, 'products': products})


def sorted_basket(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except ObjectDoesNotExist:
        return HttpResponse('Клиент не найден')
    product_set = []
    for delta in [7, 30, 365]:
        td = datetime.today() - timedelta(days=delta)
        product_set.append(Products.objects.filter(order__client=client, order__order_date__gt=td).distinct())
    product_count = [i.count() for i in product_set]
    return render(request, 'storeapp/all_products.html',
                  {'client': client, 'product_set': product_set, 'product_count': product_count})

