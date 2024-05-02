from django.contrib import admin

# Register your models here.

from .models import (
    Product, Category, Order, OrderItem, Customer, 
    Promotion, PromotionCode, Stock
)

# Register your models here
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(Promotion)
admin.site.register(PromotionCode)
admin.site.register(Stock)
