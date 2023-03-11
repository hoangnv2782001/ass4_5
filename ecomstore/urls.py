"""ecomstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
import preview.views
import catalog.urls
import cart.urls
from .views import file_not_found_404
import accounts.urls

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("catalog/",preview.views.home),
    path('catalog/',include(catalog.urls)),
    path('cart/',include(cart.urls)),
    # path('accounts/', include(accounts.urls)),
    path('ccounts/', include('django.contrib.auth.urls')),
]
handler404 = file_not_found_404
