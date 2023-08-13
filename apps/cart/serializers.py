from rest_framework import serializers
from .models import Cart, CartItem
from apps.product.serializers import VariantSerializer


class CartItemSerializer(serializers.ModelSerializer):

    total = serializers.SerializerMethodField('get_sub_total')
    variant_data = VariantSerializer(source='variant_id', read_only=True)
    
    def get_sub_total(self, obj):
        return obj.sub_total

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    cart_items = serializers.SerializerMethodField('get_cart_items')
    total_items = serializers.SerializerMethodField('get_total_items')
    total = serializers.SerializerMethodField('get_total')


    def get_cart_items(self, obj):
        serializer_context = {'request': self.context.get('request')}
        cart_items = obj.cart_items.all()
        return CartItemSerializer(cart_items, many=True, context=serializer_context).data

    def get_total_items(self, obj):
        return obj.count_cart_items_set

    def get_total(self, obj):
        return obj.total_amount

    class Meta:
        model = Cart
        fields = ['id',
                  'user_id',
                  'created',
                  'updated',
                  'total_items',
                  'total',
                  'cart_items',
                  ]
