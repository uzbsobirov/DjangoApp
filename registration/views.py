from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Register
from .validators import Validator
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

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
                form.save()
            return redirect("shop:product_list")
        else:
            return render(request, template_name=self.template_name, context={'valid': False})




def login(request):
    print(request.POST)
    form = Validator(Register)
    context = request.POST

    if request.method == 'POST':
        form = Validator(Register, request.POST)
        if form.is_true():
            return redirect('shop:product_list')
        else:
            return render(request, 'registration/login.html', {'context': context, 'valid': form.is_true()})
    return render(request, 'registration/login.html', {'context': context, 'valid': True})

def login_request(request):
	if request.method == "POST":
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				return redirect("shop:product_list")
			else:
				return render(request=request, template_name="registration/login.html")
		else:
			return render(request=request, template_name="registration/login.html")
	form = LoginForm()
	return render(request=request, template_name="registration/login.html", context={"form":form})