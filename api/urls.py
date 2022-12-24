from django.urls import path
from .views import ProductListCreateAPIView


urlpatterns = [
    path('', ProductListCreateAPIView.as_view())
]