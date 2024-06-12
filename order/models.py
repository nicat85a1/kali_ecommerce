from django.db import models
from core.models import TimeStampedModel
from user.models import User
from product.models import Product

# Create your models here.

class Order(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    first_name = models.CharField(max_length=55,blank=True)
    last_name = models.CharField(max_length=55,blank=True)
    phone = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def create_invoice(self):
        invoice = Invoice.objects.create(order=self,quantity=self.quantity,price=self.product.price*self.quantity)
        return invoice

class Invoice(TimeStampedModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=255)