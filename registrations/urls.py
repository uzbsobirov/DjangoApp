from django.urls import path
from .views import *

app_name = "registrations"

urlpatterns = [
    path('register/', RegisterClass.as_view(), name="register")
]