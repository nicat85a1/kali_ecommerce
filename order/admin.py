from django.contrib import admin

from order.models import Order,Invoice

admin.site.register(Order)
admin.site.register(Invoice)