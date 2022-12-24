from django.urls import path
from .views import contact

app_name = 'others'



urlpatterns = [
    path('', contact, name="contact")
]