from django.conf import settings


from django.db import models

# Create your models here.
#stripe.api_key = settings.STRIPE_SECRET_KEY

class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=120)

    def __str__(self):
        return str(self.stripe_id)
 
    