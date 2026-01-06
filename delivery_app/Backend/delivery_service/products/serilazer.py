from rest_framework import serializers
from .models import Category,Product

class CategorySerilazer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProductSerilazer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'