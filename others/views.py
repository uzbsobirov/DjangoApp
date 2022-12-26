from django.shortcuts import render, redirect

def contact(request):
    return render(request=request, template_name="contact.html")


