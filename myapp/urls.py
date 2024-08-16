"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('blog', views.blog, name='blog'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('main', views.main, name='main'),
    path('product_details/<int:id>', views.product_details, name='product_details'),
    path('shop_cart', views.shop_cart, name='shop_cart'),
    path('ragister', views.ragister, name='ragister'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search_fun', views.search_fun, name='search_fun'),
    path('forgot', views.forgot, name='forgot'),
    path('confirm', views.confirm, name='confirm'),
    path('pricefilter', views.pricefilter, name='pricefilter'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('cart_plus/<int:id>', views.cart_plus, name='cart_plus'),
    path('cart_minus/<int:id>', views.cart_minus, name='cart_minus'),
    path('cart_remove/<int:id>', views.cart_remove, name='cart_remove'),
    path('billing_address', views.billing_address, name='billing_address'),

    
    
]
