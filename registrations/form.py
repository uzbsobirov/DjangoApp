from django import forms
from .models import RegisterModel

class RegisterForm(forms.ModelForm):
    confirm = forms.CharField(max_length=100)
    class Meta:
        model = RegisterModel
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm']
            