from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ProductForm
from .models import Product


class ProductCreateView(CreateView):
    """Функция для создания продукта через форму."""
    model = Product
    form_class = ProductForm
    template_name = 'create.html'
    success_url = reverse_lazy('product:product')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Product.objects.order_by('id')
        return super(ProductCreateView, self).get_context_data(**kwargs)
