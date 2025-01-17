from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate_price(self, value):
        """Validation price"""
        if value <= 0:
            raise serializers.ValidationError('The price must be positive')
        return value
