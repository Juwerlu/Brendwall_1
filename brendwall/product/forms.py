from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """Форма для создания продукта."""

    class Meta:
        model = Product
        fields = '__all__'
