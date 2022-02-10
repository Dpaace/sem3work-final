from django.contrib import admin
from .models import Cart, CartItem, Orders
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_id", "date_added", )

class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "cart", "is_active")

class OrdersAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "status")
    list_editable = ("status",)

admin.site.register(Cart, CartAdmin)

admin.site.register(CartItem, CartItemAdmin)

admin.site.register(Orders, OrdersAdmin)