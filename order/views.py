from django.shortcuts import redirect, get_object_or_404
from order.models import Order
from django.db import IntegrityError
# Create your views here.

def create_order(request, product_id,quantity):
    """print(request.user,"aaaaaaaaaaaa")
    if request.user == "AnonymousUser":
        return redirect('login_views')"""
    """if request.user.is_anonymous:
        return redirect("login_views")
    print(product_id,"aaaaaaaaaaaaaaaaa")"""
    try:
        order = Order.objects.create(product_id=product_id, quantity=quantity)
        order.create_invoice()
    except IntegrityError:
        return redirect('home')
    
    return redirect('home')

# sayisiz order