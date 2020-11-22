from decimal import Decimal
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from accounts.models import UserAddress
# Create your models here.

from carts.models import Cart

User = get_user_model()

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)

#python tuples
try:
    tax_rate = settings.DEFAULT_TAX_RATE
except Exception as e:
    print(str(e))
    raise NotImplementedError(str(e))    

class Order(models.Model):
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    # address
    billing_address = models.ForeignKey(UserAddress, default=1, related_name='billing_address', on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(UserAddress, default=1, related_name='shipping_address', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.order_id
    
    def get_final_amount(self):
        instance = Order.objects.get(id=self.id)
        two_places = Decimal(10) ** -2
        tax_rate_dec = Decimal("%s" %(tax_rate))
        sub_total_dec = Decimal(self.sub_total)
        tax_total_dec = Decimal(tax_rate_dec * sub_total_dec).quantize(two_places)
        instance.tax_total = tax_total_dec
        instance.final_total = sub_total_dec + tax_total_dec
        instance.save()
        return instance.final_total
