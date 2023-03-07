from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from catalog.models import Category, Product


def file_not_found_404(request,exception):
    page_title = 'Page Not Found'
    return render(request, '404.html', locals(),status=404)
