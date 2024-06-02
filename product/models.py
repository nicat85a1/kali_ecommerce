from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField("product_image",null=True,blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True,null=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name