from rest_framework.serializers import ModelSerializer
from order_products.models import OrderProduct
from products.models import Product
from orders.models import Order


class _ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class _OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderProductSerializer(ModelSerializer):
    product = _ProductSerializer(read_only=True)
    order = _OrderSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        fields = '__all__'
