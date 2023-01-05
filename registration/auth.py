from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from .models import Register

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        # UserModel = get_user_model()
        try:
            user = Register.objects.get(email=email)
        except Register.DoesNotExist:
            return None
        else:
            if password == user.password:
                return user
            else:
                return None
        