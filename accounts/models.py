import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.signals import user_logged_in
from django.urls import reverse

from django.db import models

# Create your models here.
stripe.api_key = settings.STRIPE_SECRET_KEY
from django.template.loader import render_to_string

class UserAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=25)
    phone = models.CharField(max_length=120)
    shipping = models.BooleanField(default=True)
    billing = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) 

    def __str__(self):
        return str(self.user.username)
     


class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.stripe_id)

    
'''def get_or_create_stripe(sender, user, *args, **kwargs):
    try:
        user.userstripe.stripe_id
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(
            email = str(user.email)
        )
        new_user_stripe = UserStripe.objects.create(
            user=user,
            stripe_id = customer.id
        )
    except:
        pass

user_logged_in.connect(get_or_create_stripe) 
'''

class EmailConfirmed(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=200, null=True, blank=True)
    confirmed = models.BooleanField(default=False)   

    def __str__(self):
        return str(self.confirmed)

    def active_user_email(self):
        # send email here & render a string
        activation_url = "%s/%s" %(settings.SITE_URL, reverse("activation_view", args=[self.activation_key]))
       # activation_url = "http://127.0.0.1:8000/accounts/activate/%s" %(self.activation_key)
        context = {
            "activation_key": self.activation_key,
            "activation_url": activation_url,
        }
        message = render_to_string("accounts/activation_message.txt", context)
        subject = "Activate your email"
        print(message)
        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
        
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.user.email], kwargs)     
         
    

class EmailMarketingSignUp(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)    

    def __str__(self):
        return str(self.email)