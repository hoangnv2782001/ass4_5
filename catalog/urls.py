from django.conf.urls import *
from django.urls import path
from catalog import  views
urlpatterns = [
    path('', views.index, {'template_name': 'catalog/index.html'}, 'catalog_home'),
    path('category/<slug:category_slug', views.show_category, {'template_name': 'catalog/category.html'}, 'catalog_category'),
    path('product/<slug:product_slug>/',views.show_product, {'template_name': 'catalog/product.html'}, 'catalog_product'),
]
