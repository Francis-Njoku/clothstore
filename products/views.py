from django.shortcuts import render
from django.http import Http404


# Create your views here.

from .models import Product, ProductImage

def home(request):
    '''
    if request.user.is_authenticated:
        username_is = "Francis Xavier using context"
        context = {"username_is": username_is}
    else:
        context = {"username_is": "Unknown"}'''
    products = Product.objects.all()
    context = {"products": products}
    template = 'products/home.html'
    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)

def single(request, slug):
    #try:
        product = Product.objects.get(slug=slug)
        #images = product.productimage_set.all()
        images = ProductImage.objects.filter(product=product)
        print(images)

        context = {'product': product, "images": images}
        template = 'products/single2.html'
        return render(request, template, context)
    #except:
     #   raise Http404        

