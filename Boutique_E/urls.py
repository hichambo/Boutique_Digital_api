from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet, CategoryViewSet, OrderViewSet, 
    OrderItemViewSet, CustomerViewSet, PromotionViewSet, 
    PromotionCodeViewSet, StockViewSet
)
router = DefaultRouter()

# Register viewsets with the router
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('orders', OrderViewSet)
router.register('order-items', OrderItemViewSet)
router.register('customers', CustomerViewSet)
router.register('promotions', PromotionViewSet)
router.register('promotion-codes', PromotionCodeViewSet)
router.register('stock', StockViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
