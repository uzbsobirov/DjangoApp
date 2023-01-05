from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Register
from .validators import Validator
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .auth import EmailBackend


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
    return render(request=request, template_name="registration/register.html")

class RegisterClass(View):
    template_name = "registration/register.html"
    def get(self, request):
        return render(request=request, template_name=self.template_name)
    def post(self, request):
        form = Validator(Register, request.POST)
        if form.is_valid():
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user=user)
            return redirect("registration:login")
        else:
            return render(request, template_name=self.template_name, context={'valid': False})

class LoginView(View):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        print(email, password)
        user = authenticate(self, request=request, email=email.lower(), password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('shop:product_list')
        else:
            return HttpResponse('error')