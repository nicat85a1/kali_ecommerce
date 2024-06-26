from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel

# Create your models here.

class Product(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField("product_image",null=True,blank=True)
    description = models.TextField()
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True,null=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name