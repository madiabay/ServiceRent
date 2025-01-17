import uuid
from typing import Protocol
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from products.models import Product


class ProductRepositoryInterface(Protocol):
    @staticmethod
    def get_products() -> QuerySet[Product]: ...

    @staticmethod
    def get_product(product_uuid: str) -> Product: ...

    @staticmethod
    def create_product(product_data) -> Product: ...


class ProductRepositoryV1:
    @staticmethod
    def get_products() -> QuerySet[Product]:
        return Product.objects.all()

    @staticmethod
    def get_product(product_uuid: str) -> Product:
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=uuid.UUID(product_uuid))
        return product

    @staticmethod
    def create_product(product_data) -> Product:
        return Product.objects.create(**product_data)
