from django.urls import path
from .views import index, basket, sorted_basket

urlpatterns = [
    path('index/<int:product_id>/', index, name='index'),
    path('all_orders/<int:client_id>/', basket, name='basket'),
    path('all_products/<int:client_id>/', sorted_basket, name='sorted_basket'),
]
