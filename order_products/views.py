from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.views import APIView
from django.utils.dateparse import parse_datetime

from order_products.models import OrderProduct
from order_products.serializers import OrderProductSerializer
from order_products.services import OrderProductServiceV1

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class OrderProductViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderProductStatisticViewSet(APIView):
    order_product_service = OrderProductServiceV1()

    start_time_param = openapi.Parameter(
        'start_time',
        openapi.IN_QUERY,
        description='Начальное время периода',
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME,
        default="2024-01-01T00:00:00Z",
    )

    end_time_param = openapi.Parameter(
        'end_time',
        openapi.IN_QUERY,
        description='Конечное время периода',
        type=openapi.TYPE_STRING,
        format=openapi.FORMAT_DATETIME,
        default="2024-01-01T00:00:00Z",
    )

    @swagger_auto_schema(
        manual_parameters=[start_time_param, end_time_param],
    )
    def get(self, request):
        breakpoint()
        try:
            # get periods from query_params
            start_time = parse_datetime(request.query_params.get('start_time'))
            end_time = parse_datetime(request.query_params.get('end_time'))

            if not all((start_time, end_time)):
                return Response(
                    {"error": "Необходимо указать start_time и end_time"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if start_time >= end_time:
                return Response(
                    {"error": "start_time должно быть меньше end_time"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            statistics = self.order_product_service.get_statistics(start_time, end_time)
            return Response(statistics, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
