from django.shortcuts import render
from .serializers import ProductSerializer, categorySerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from shop.models import Product
from rest_framework import status

class ProductListCreateAPIView(APIView):
    def get(slef, request):
        products = Product.objects.all()
        serializer = ProductSerializer(instance=products, many=True)
        return Response(data=serializer.data)

    def post(slef, request):
        data = request.data
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
