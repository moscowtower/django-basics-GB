from django.contrib import admin
from ordersapp.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'is_active','created', 'updated')
    readonly_fields = ('created', 'updated')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product','quantity')