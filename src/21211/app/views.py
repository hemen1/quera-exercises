from django.http import response
from django.shortcuts import get_object_or_404

from .models import *


def checkout(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    orders = OrderItem.objects.filter(order=order)
    total_price = 0
    for each_order in orders:
        total_price += each_order.product.price * each_order.quantity

    return response.JsonResponse({'total_price': "{.2f}".format(total_price)})
