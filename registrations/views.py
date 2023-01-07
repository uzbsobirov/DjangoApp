from django.shortcuts import render, redirect
from django.views import View
from .form import RegisterForm

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
    pass
        
