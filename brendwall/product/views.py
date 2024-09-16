from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ProductForm
from .models import Product


class ProductCreateView(CreateView, ListView):
    """Функция для создания продукта через форму."""
    model = Product
    form_class = ProductForm
    template_name = 'create.html'
    success_url = reverse_lazy('product:product')
    context_object_name = 'object_list'
