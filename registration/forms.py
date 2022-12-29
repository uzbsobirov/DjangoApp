from .models import Register, Login
from django.forms import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = "__all__"

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = "__all__"