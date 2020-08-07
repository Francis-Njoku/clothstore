from django.db import models
from django.urls import reverse

# Create your models here.

from carts.models import Cart

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.order_id
    
