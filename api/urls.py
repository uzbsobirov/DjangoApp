from django.urls import path
from .views import ProductListCreateAPIView,ProductRetrieveUpdateDeleteAPIView, CategoryRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView, PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('product/<slug:slug>/', ProductRetrieveUpdateDeleteAPIView.as_view()),
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('posts/', PostListCreateAPIView.as_view()),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view())
]