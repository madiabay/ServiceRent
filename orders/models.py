import uuid
from django.db import models


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='Order ID')
    start_date = models.DateTimeField(verbose_name="Rental Start Date")
    end_date = models.DateTimeField(verbose_name="Rental End Date")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total Price')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ('-created_at',)
