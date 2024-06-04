from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from order.models import Order, Invoice
# Create your views here.

"""def dashboard_view(request):
    if not request.user.is_authenticated:
        return HttpResponse("Get login ol")
    return render(request, 'dashboard/dashboard.html')"""

@login_required(login_url='login_views')
def dashboard_view(request):
    orders = Order.objects.filter(user=request.user)
   
    context = {
        'orders': orders,
        }
    return render(request, 'dashboard/dashboard.html', context)