from django.shortcuts import render, redirect
from django.views import View
from .form import RegisterForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf.global_settings import LOGIN_URL, EMAIL_HOST_USER, AUTH_USER_MODEL
from django.contrib.auth.hashers import make_password, check_password


class RegisterClass(View):
    template_name = 'registration/register.html'
    def get(self, request):
        return render(request=request, template_name=self.template_name)
    
    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(password=password)
            user.save()
            login(request, user)
            return redirect("shop:product_list")
        else:
            return redirect("registrations:register")


class LoginClass(View):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)
        
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = authenticate(request, username=email.lower(), password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('shop:product_list')
        else:
            return HttpResponse('error')


class Logout(LoginRequiredMixin, View):
    login_url = LOGIN_URL

    def get(self, request):
        logout(request=request)
        return redirect("shop:product_list")