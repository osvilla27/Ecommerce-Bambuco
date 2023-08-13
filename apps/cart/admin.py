from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated')
    ordering = ('-updated',)
    

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'product_id', 'quantity', 'status')
    ordering = ('-updated',)


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)