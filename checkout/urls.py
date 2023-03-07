from django.urls import include, path
from ecomstore import settings
urlpatterns = [
    path('', 'show_checkout', {'template_name': 'checkout/checkout.html','SSL': settings.ENABLE_SSL}, 'checkout'),
    path('receipt', 'receipt', {'template_name': 'checkout/receipt.html',
                                'SSL': settings.ENABLE_SSL}, 'checkout_receipt'),
]
