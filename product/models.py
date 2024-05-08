from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True,null=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name