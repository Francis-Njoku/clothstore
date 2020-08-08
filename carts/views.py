from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Cart, CartItem
from products.models import Product, Variation

def view(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart": cart}
        # Update details
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
            
        request.session['items_total'] = cart.cartitem_set.count()
        #print(cart.cartitem_set.count())
        cart.total = new_total
        cart.save() 
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

def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart  =Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))

    cartitem = CartItem.objects.get(id=id)
    cartitem.delete()
    # Remove id from database
    #cartitem.cart= None
    # cartitem.save()
    return HttpResponseRedirect(reverse("cart"))            

def add_to_cart(request, slug):
    #cart = Cart.objects.all()[0]
    # use session to update cart

    # expire session
    request.session.set_expiry(3000000)

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

    product_var = [] # product variation    
    if request.method == "POST":
        qty = request.POST['qty']
        
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.objects.get(product = product, category__iexact=key, title__iexact=val)
                product_var.append(v)              
            except:
                pass     
        # check if cart item is created and create if not exist
        cart_item = CartItem.objects.create(cart=cart, product=product)
        if len(product_var) > 0:
            #cart_item.variations.clear()
            cart_item.variations.add(*product_var)
        cart_item.quantity = qty
        cart_item.save()
        
        return HttpResponseRedirect(reverse("cart"))  
    else:
        return HttpResponseRedirect(reverse("cart"))      

    #print(qty)
    #print(int(qty))            



    # Update total
     # Update product to cart
            
    '''     
    
    if not cart_item in cart.cartitem_set.all():
            cart.items.add(cart_item)
        else:
            cart.items.remove(cart_item)
    ''' 

    # Return to cart     
    return HttpResponseRedirect(reverse("cart"))        