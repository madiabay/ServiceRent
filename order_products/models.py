import uuid
from django.db import models

from orders.models import Order
from products.models import Product


class OrderProduct(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='Order Product ID')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Order", related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Product', related_name='order_products')
    rendal_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Rendal Price')
    rendal_duration = models.PositiveIntegerField(verbose_name='Rental Duration')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['order', 'product'], name='unique_order_product')
        ]
