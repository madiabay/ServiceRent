from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from orders.serializers import OrderSerializer, CreateOrderSerializer
from orders.repositories import OrderRepositoryInterface, OrderRepositoryV1


class OrderViewSet(viewsets.ViewSet):
    order_repository: OrderRepositoryInterface = OrderRepositoryV1()

    def list(self, request):
        queryset = self.order_repository.get_orders()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk: str = None):
        order = self.order_repository.get_order(order_uuid=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CreateOrderSerializer)
    def create(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_order = self.order_repository.create_order(data=serializer.validated_data)
        return Response(OrderSerializer(new_order).data, status=status.HTTP_201_CREATED)
