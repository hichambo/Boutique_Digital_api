from django.shortcuts import render
from rest_framework import  permissions


# Create your views here.
from rest_framework import viewsets
from .models import (
    Product, Category, Order, OrderItem, Customer, 
    Promotion, PromotionCode, Stock
)
from .serializers import (
    ProductSerializer, CategorySerializer, OrderSerializer, 
    OrderItemSerializer, CustomerSerializer, PromotionSerializer, 
    PromotionCodeSerializer, StockSerializer
)
from .permissions import (
    IsAdminOrReadOnly, IsOwnerOrReadOnly
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ permissions.IsAdminOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can manage orders

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only order owners can manage order items

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Users can only manage their own profiles

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admins only for promotion management

class PromotionCodeViewSet(viewsets.ModelViewSet):
    queryset = PromotionCode.objects.all()
    serializer_class = PromotionCodeSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admins only for promotion code management

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminOrReadOnly]  # Admins only for stock management
