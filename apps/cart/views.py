from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer


class CartApiViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['id', 'status']
    ordering = ['-created']


class CartItemApiViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['id', 'status']
    ordering = ['-created']
