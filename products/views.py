from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from products.serializers import ProductSerializer
from products.repositories import ProductRepositoryInterface, ProductRepositoryV1


class ProductViewSet(viewsets.ViewSet):
    product_repository: ProductRepositoryInterface = ProductRepositoryV1()

    def list(self, request):
        queryset = self.product_repository.get_products()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, id: str = None):
        product = self.product_repository.get_product(product_uuid=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ProductSerializer)
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_product = self.product_repository.create_product(product_data=serializer.validated_data)
        return Response(ProductSerializer(new_product).data, status=status.HTTP_201_CREATED)
