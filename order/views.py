from django.shortcuts import redirect, get_object_or_404
from order.models import Order
# Create your views here.

def create_order(request, product_id,quantity):
    order=Order.objects.create(user=request.user,product_id=product_id,quantity=quantity)
    order.create_invoice()
    return redirect('home')