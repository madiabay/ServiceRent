from django.urls import path, include


urlpatterns = [
    path('v1/', include('products.urls')),
    path('v1/', include('orders.urls')),
    path('v1/', include('order_products.urls')),
]
