from django.urls import path
from .views import *

app_name = "registrations"

urlpatterns = [
    path('register/', RegisterClass.as_view(), name="register"),
    path('login/', LoginClass.as_view(), name='login'),
    path('logout/', Logout.as_view(), name="logout")
]