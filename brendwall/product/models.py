from django.db import models

from .validators import poz_price


class Product(models.Model):
    """Модель продукта."""
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=8,
                                decimal_places=1,
                                default=0.0, validators=(poz_price,))

    def __str__(self):
        return self.name
