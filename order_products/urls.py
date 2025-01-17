from rest_framework.routers import DefaultRouter
from django.urls import path, include
from order_products.views import OrderProductViewSet

from order_products.views import OrderProductStatisticViewSet


router = DefaultRouter()
router.register(r'order_products', OrderProductViewSet, basename='order_products')

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/order_products/statistics/', OrderProductStatisticViewSet.as_view(), name='statistics'),
]
