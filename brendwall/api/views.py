from product.models import Product
from rest_framework import mixins, viewsets

from .serializers import ProductSerializer


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Составной ViewSet для создания и отображения объектов."""
    pass


class ProductViewSet(CreateListViewSet):
    """ViewSet для управления продуктами в API."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
