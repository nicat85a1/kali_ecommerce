from django.shortcuts import redirect, get_object_or_404, render
from order.models import Order, Product
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.
from order.forms import OrderForm
from core.utils.stripe import Stripe

#@login_required(login_url='login_views')
def create_order(request, product_id,quantity):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone = form.cleaned_data['phone']
        address = form.cleaned_data['address']
        order = Order.objects.create(user=request.user,product_id=product_id, 
                                     quantity=quantity,first_name=first_name,
                                     last_name=last_name,phone=phone,address=address)
        invoice = order.create_invoice()
        product = Product.objects.get(id=product_id)
        stripe = Stripe()
        stripe.transaction(amount=product.price*quantity)
        invoice.transaction_id = stripe.__transaction_id()
        invoice.save()
        return redirect(stripe.get_payment_url())

    return render(request,"product/buy_product.html",{'form':form})