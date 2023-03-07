from django.contrib import admin
from django.urls import path,include
import preview.views
import catalog.urls
import cart.urls
from cart import views

urlpatterns =[
    path('',views.show_cart, { 'template_name': 'cart/cart.html' }, 'show_cart'),
]