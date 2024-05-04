"""Project_Api_boutique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import your views here
from Boutique_E.views import (
    ProductViewSet, CategoryViewSet, OrderViewSet, OrderItemViewSet, 
    CustomerViewSet, PromotionViewSet, PromotionCodeViewSet, StockViewSet
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
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
