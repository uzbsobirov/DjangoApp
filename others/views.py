from django.shortcuts import render, redirect
from django.views.generic import TemplateView

def contact(request):
    return render(request=request, template_name="contact.html")


def wishlist(request):
    return render(request=request, template_name="wishlist.html")


def register(request):
    return render(request=request, template_name="registration/register.html")

def login(request):
    return render(request=request, template_name="registration/login.html")
    

def checkout(request):
    return render(request=request, template_name="checkout.html")


def about_us(request):
    return render(request=request, template_name="about.html")