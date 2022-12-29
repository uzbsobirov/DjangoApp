from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Register
from .validators import Validator


def register(request):
    print(request.POST)
    form = Validator(Register)
    if request.method == 'POST':
        form = Validator(Register, request.POST)
        if form.is_valid():
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("shop:product_list")
    return render(request=request, template_name="signin.html")


def login(request):
    form = Validator(Register)
    context = request.POST

    if request.method == 'POST':
        form = Validator(Register, request.POST)
        if form.is_true():
            return redirect('shop:product_list')
        else:
            return render(request, 'signin.html', {'context': context, 'valid': form.is_true()})
    return render(request, 'signin.html', {'context': context, 'valid': True})

