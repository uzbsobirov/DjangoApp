from django.shortcuts import render, redirect
from django.views.generic import TemplateView

def contact(request):
    return render(request=request, template_name="contact.html")

def wishlist(request):
    return render(request=request, template_name="wishlist.html")


def signin(request):
    return render(request=request, template_name="signin.html")
    
