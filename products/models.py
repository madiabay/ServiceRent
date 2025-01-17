import uuid
from django.db import models


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='Product ID')
    name = models.CharField(max_length=255, unique=True, verbose_name='Product Name')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Product Price Per Hour')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = 'name', '-created_at'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
