from django.shortcuts import render, redirect
from django.views import View
from .form import RegisterForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponse

class RegisterClass(View):
    template_name = 'registration/register.html'
    def get(self, request):
        return render(request=request, template_name=self.template_name)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
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
        user = authenticate(request, email=email.lower(), password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:product_list')
        else:
            return HttpResponse('error')
