from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet

router_v1 = DefaultRouter()

router_v1.register('products', ProductViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
