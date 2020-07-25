from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Cart, CartItem
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
    request.session.set_expiry(3000000)

    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        qty = request.GET.get('qty')
    except:
        qty = None
        update_qty = False        

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)   
    print('chima1')

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    print('chima2')

    # check if cart item is created and create if not exist
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        print("yeah")   

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass        
    print(qty)
    print(int(qty))            

    # Update product to cart
    #if not cart_item in cart.items.all():
    #    cart.items.add(cart_item)
    #else:
     #   cart.items.remove(cart_item)

    # Update total
    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        print(item.product.price)
        print(float(item.product.price))
        new_total += line_total

    request.session['items_total'] = cart.cartitem_set.count()
    print(cart.cartitem_set.count())
    cart.total = new_total
    cart.save()    

    # Return to cart     
    return HttpResponseRedirect(reverse("cart"))        