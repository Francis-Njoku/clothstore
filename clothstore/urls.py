from products import views
from carts import views as cart_view
from orders import views as order_view
"""clothstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('s/', views.search, name='search'),
    path('', views.home, name='home'),
    path('products/', views.all, name='products'),
    path('cart/', cart_view.view, name='cart'),
    path('checkout/', order_view.checkout, name='checkout'),
    path('orders/', order_view.orders, name='orders'),
    path('cart/<int:id>', cart_view.remove_from_cart, name='remove_from_cart'),
    path('cart/<slug:slug>', cart_view.add_to_cart, name='add_to_cart'),
    path('products/<slug:slug>', views.single, name='single_product')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('s/', views.search, name='search'),
    path('', views.home, name='home'),
    path('products/', views.all, name='products'),
    path('cart/', cart_view.view, name='cart'),
    path('orders/', order_view.orders, name='orders'),
    path('checkout/', order_view.checkout, name='checkout'),
    path('cart/<int:id>', cart_view.remove_from_cart, name='remove_from_cart'),
    path('cart/<slug:slug>', cart_view.add_to_cart, name='add_to_cart'),
    path('products/<slug:slug>', views.single, name='single_product')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

