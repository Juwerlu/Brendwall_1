from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path(
        '',
        views.ProductCreateView.as_view(),
        name='product'
    ),
]
