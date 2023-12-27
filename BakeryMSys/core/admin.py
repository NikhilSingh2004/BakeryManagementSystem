from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "order_name", "order_date", "order_quantity")

admin.site.register(Order, OrderAdmin)