from django.core.exceptions import ValidationError


def poz_price(value):
    """Валидатор, который проверяет, что цена не отрицательная."""
    if value < 0:
        raise ValidationError('Цена не может быть отрицательной!')
