import uuid
from typing import Protocol
from django.db import transaction
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from orders.models import Order
from products.models import Product
from order_products.models import OrderProduct


class OrderRepositoryInterface(Protocol):
    @staticmethod
    def get_orders() -> QuerySet[Order]: ...

    @staticmethod
    def get_order(order_uuid: str) -> Order: ...

    @staticmethod
    def create_order(data: dict) -> Order: ...


class OrderRepositoryV1:
    @staticmethod
    def get_orders() -> QuerySet[Order]:
        return Order.objects.all()

    @staticmethod
    def get_order(order_uuid: str) -> Order:
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=uuid.UUID(order_uuid))
        return order

    @staticmethod
    def create_order(data: dict) -> Order:
        """
        Args:
        start_date: Начало аренды
        end_date: Конец аренды
        product_id: UUID продукта

        Returns:
            Order
        """
        product = get_object_or_404(Product, pk=data['product_id'])
        duration = data['end_date'] - data['start_date']
        duration = int(duration.total_seconds() / 3600)
        total_price = product.price * duration

        # на последний заказ смотрим, потому что по дефолту сортируется по ordering = ('-created_at',)
        last_order_end_date = (Order.objects.prefetch_related('order_products')
                               .filter(order_products__product_id=product.id)
                               .first())
        if last_order_end_date and last_order_end_date.end_date >= data['start_date']:
            raise ValidationError('Продукт все еще в аренде')  # ВТОРОЕ УСЛОВИЕ

        with transaction.atomic():  # ДОПОЛНИТЕЛЬНОЕ ТРЕБОВАНИЯ
            order = Order.objects.create(
                start_date=data['start_date'],
                end_date=data['end_date'],
                total_price=total_price,
            )
            OrderProduct.objects.create(
                order=order,
                product=product,
                rendal_price=total_price,
                rendal_duration=duration,
            )

        return order
