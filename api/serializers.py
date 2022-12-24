from rest_framework import serializers
from shop.models import Product, Category



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'slug', 'image', 'description', 'price', 'available', 'rating', 'discount']

class categorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"