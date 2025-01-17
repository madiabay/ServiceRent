from rest_framework_nested import routers
from django.urls import path, include
from orders.views import OrderViewSet
from order_products.views import OrderProductViewSet


router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet, basename='orders')

nested_order_products_router = routers.NestedSimpleRouter(router, r'orders', lookup='order')
nested_order_products_router.register(r'products', OrderProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_order_products_router.urls)),
]
