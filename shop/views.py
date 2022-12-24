from django.shortcuts import render, get_object_or_404
from .models import *


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all()
    return render(request, "shop/list.html", {'category':category, 'categories':categories, 'products':products})



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, "shop/detail.html", {"product":product})