from rest_framework import serializers
from order_products.models import OrderProduct


class _OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    order_products = _OrderProductSerializer(read_only=True, many=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate(self, data):
        """Validation order data"""
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("The end date must be later than the start date.")
        return data

    def validate_total_price(self, value):
        """Validation total price"""
        if value <= 0:
            raise serializers.ValidationError("The total cost must be positive.")
        return value


class CreateOrderSerializer(OrderSerializer):
    product_id = serializers.UUIDField(write_only=True)
