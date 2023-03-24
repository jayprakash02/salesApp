from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from .models import SalesRepresentative, Store, Product, Order, OrderItem
from .serializers import (
    SalesRepresentativeSerializer, StoreSerializer, ProductSerializer,
    OrderSerializer, OrderItemSerializer
)

class SalesRepresentativeViewSet(viewsets.ModelViewSet):
    queryset = SalesRepresentative.objects.all()
    serializer_class = SalesRepresentativeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'email']
    filterset_fields = ['name', 'email']


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'address', 'phone_number', 'email']
    filterset_fields = ['name', 'address', 'phone_number', 'email']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'category']
    filterset_fields = ['name', 'category']


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['store__name', 'sales_rep__name', 'delivery_date', 'payment_terms', 'shipping_address', 'notes']
    filterset_fields = ['store', 'sales_rep', 'delivery_date']
