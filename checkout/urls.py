from django.urls import include, path
from ecomstore import settings
from checkout import views
urlpatterns = [
    path('', views.show_checkout , {'template_name': 'checkout/checkout.html'}, 'checkout'),
    path('receipt/', views.receipt, {'template_name': 'checkout/receipt.html'}, 'checkout_receipt'),
]
