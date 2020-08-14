import stripe

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save

from .models import UserStripe

stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model


# If we decide to change how we want to add the stripe id, this is where we set it for a user_logged_in
'''def get_or_create_stripe(sender, user, *arg, **kwargs):
    print(sender)
    print(user) 
    try:
        user.userstripe.stripe_id
        print(user.userstripe.stripe_id)
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(
            #description="My First Test Charge (created for API docs)",
            email = str(user.email)
        )    
        new_user_stripe = UserStripe.objects.create(
            user=user,
            stripe_id=customer.id
        )   
    except:
        pass  '''  
    
def get_create_stripe(user):
    '''try:
        user.userstripe.stripe_id
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(
            email = str(user.email)
        )    
        new_user_stripe = UserStripe.objects.create(
            user=user,
            stripe_id=customer.id
        )   
    except:
        pass'''
    new_user_stripe, created = UserStripe.objects.get_or_create(user=user)
    if created:
        customer = stripe.Customer.create(
            email = str(user.email)
        )
        if customer:
            print('Exist')
        else:
            print('Does not exist')    
        new_user_stripe.stripe_id = customer.id
        #snew_user_stripe.user = user
        #print(user)
        #print(customer.id)
        new_user_stripe.save()


def user_created(sender, instance, created, *args, **kwargs):
    user = instance
    if created:
        get_create_stripe(user)
        # send our email
        #
    print(sender)
    print(instance)
    print(created)

post_save.connect(user_created, sender=User)