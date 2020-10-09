from django.shortcuts import render
from django.http import Http404


# Create your views here.
from marketing.models import MarketingMessage, Slider
from .models import Product, ProductImage
from marketing.forms import EmailForm

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query': q, 'products': products}
        template = 'products/result.html'
    else:
        template = 'products/home.html'
        context = {}       
    return render(request, template, context)

def home(request):
    '''
    if request.user.is_authenticated:
        username_is = "Francis Xavier using context"
        context = {"username_is": username_is}
    else:
        context = {"username_is": "Unknown"}'''
    sliders = Slider.objects.all_featured()    
    products = Product.objects.all()
    marketing_message = MarketingMessage.objects.all()[0]
    print(marketing_message)
    print('chima')
    template = 'products/home.html'
    context = {"products": products, 
               "marketing_message": marketing_message,
               "sliders": sliders}        
    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)

def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        #images = product.productimage_set.all()
        images = ProductImage.objects.filter(product=product)
        print(images)

        context = {'product': product, "images": images}
        template = 'products/single2.html'
        return render(request, template, context)
    except:
        raise Http404        

