from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CartApiViewSet, CartItemApiViewSet


router_cart = DefaultRouter()


router_cart.register(prefix='cart',
                     basename='cart',
                     viewset=CartApiViewSet)


router_cart.register(prefix='cart-item',
                     basename='cart-item',
                     viewset=CartItemApiViewSet)
