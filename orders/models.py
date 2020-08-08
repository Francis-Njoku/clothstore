from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

from carts.models import Cart

User = get_user_model()

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)

class Order(models.Model):
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    # address
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.order_id
    
