from django.shortcuts import render, get_object_or_404
from .serializers import ProductSerializer, CategorySerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from shop.models import Product, Category
from rest_framework import status, generics
from .models import Post
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination
from .paginations import CustomPaginations
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ProductListCreateAPIView(generics.GenericAPIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPaginations
    queryset = Product.objects.all()
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # serializer = ProductSerializer(instance=queryset, many=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)



class ProductRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = ProductSerializer
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        serializer = self.serializer_class(product)
        return Response(data=serializer.data)
    
    def put(self, request, slug):
        data = request.data
        product = get_object_or_404(Product, slug=slug)
        serializer = self.serializer_class(instance=product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def patch(self, request, slug):
        data = request.data
        product = get_object_or_404(Product, slug=slug)
        serializer = self.serializer_class(instance=product, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        return Response({"Deleted": "Product was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoriesListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPaginations
    filter_backends = [filters.SearchFilter]
    lookup_field = ['slug']
    search_fields = ['name']

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.availabled.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.availabled.all()
    # pagination_class = [IsAdminUser]
    pagination_class = LimitOffsetPagination
    