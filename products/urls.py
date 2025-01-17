from django.urls import path
from products.views import ProductViewSet


urlpatterns = [
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<str:id>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-detail'),
]


# # Second Variant
# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from products.views import ProductViewSet
#
# router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
