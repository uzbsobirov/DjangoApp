from django.shortcuts import render, get_object_or_404
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from shop.models import Product, Category
from rest_framework import status, generics

class ProductListCreateAPIView(APIView):
    serializer_class = ProductSerializer
    def get(self, request):
        products = Product.objects.all()
        serializer = self.serializer_class(instance=products, many=True)
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

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer