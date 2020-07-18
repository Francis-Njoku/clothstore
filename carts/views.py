from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Cart
from products.models import Product

def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart": cart}
    else:
        empty_message = "Your Cart is Empty, please keep shopping."
        context = {"empty": True, 'empty_message': empty_message}    
    '''
    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    '''
    template = "cart/view.html"
    return render(request, template, context)

def update_cart(request, slug):
    #cart = Cart.objects.all()[0]
    # use session to update cart

    # expire session
    request.session.set_expiry(300)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)   

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

    # Update total
    new_total = 0.00
    for item in cart.products.all():
        print(item.price)
        print(float(item.price))
        new_total += float(item.price)

    request.session['items_total'] = cart.products.count()
    print(cart.products.count())
    cart.total = new_total
    cart.save()    

    # Return to cart     
    return HttpResponseRedirect(reverse("cart"))        