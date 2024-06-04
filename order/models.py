from django.db import models
from core.models import TimeStampedModel
from user.models import User
from product.models import Product

# Create your models here.

class Order(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def create_invoice(self):
        Invoice.objects.create(order=self,quantity=self.quantity,price=self.product.price)

class Invoice(TimeStampedModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(default=0)