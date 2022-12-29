from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Register
from .validators import Validator
from django.views import View

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

class RegisterClass(View):
    template_name = "signin.html"
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
    form = Validator(Register)
    context = request.POST

    if request.method == 'POST':
        form = Validator(Register, request.POST)
        if form.is_true():
            return redirect('shop:product_list')
        else:
            return render(request, 'signin.html', {'context': context, 'valid': form.is_true()})
    return render(request, 'signin.html', {'context': context, 'valid': True})

