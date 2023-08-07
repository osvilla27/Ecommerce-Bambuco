from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductApiViewSet, ListCategoriesView


router_product = DefaultRouter()


router_product.register(prefix='products',
                      basename='products',
                      viewset=ProductApiViewSet)


urlpatterns = [
    path('categories/', ListCategoriesView.as_view()),
]