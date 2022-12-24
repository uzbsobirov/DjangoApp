from rest_framework import serializers
from shop.models import Product, Category



class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = "__all__"

class categorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"