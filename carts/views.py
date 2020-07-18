from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Cart
from products.models import Product

def view(request):
    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    template = "cart/view.html"
    return render(request, template, context)

def update_cart(request):
    cart = Cart.objects.all()[0]
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass    

    # Update product to cart
    if not product in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
    return HttpResponseRedirect(reverse("cart"))        