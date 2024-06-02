from django.urls import path
from order.views import create_order

urlpatterns = [
    path('create-order/<int:product_id>/<int:quantity>', create_order, name='create_order'),
    
    ]