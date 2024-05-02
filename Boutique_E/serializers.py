from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, Customer, Promotion, PromotionCode, Stock

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  

    class Meta:
        model = Product
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)  # Nested serializer for customer
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'



class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

class PromotionCodeSerializer(serializers.ModelSerializer):
    promotion = PromotionSerializer(read_only=True)  
    used_by = CustomerSerializer(read_only=True) 
    class Meta:
        model = PromotionCode
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Stock
        fields = '__all__'
