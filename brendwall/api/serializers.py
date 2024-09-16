from product.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Product"""

    class Meta:
        fields = '__all__'
        model = Product
