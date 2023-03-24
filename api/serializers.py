from rest_framework import serializers
from api.models import SalesRepresentative, Store, Product, Order, OrderItem


class SalesRepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRepresentative
        fields = ['id', 'name', 'email', 'password']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'phone_number', 'email', 'logo', 'sales_rep']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'store', 'sales_rep', 'delivery_date', 'payment_terms', 'shipping_address', 'notes', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item in order_items_data:
            OrderItem.objects.create(order=order, **item)
        return order

    def update(self, instance, validated_data):
        order_items_data = validated_data.pop('order_items')
        order_items = (instance.order_items).all()
        order_items = list(order_items)
        instance.store = validated_data.get('store', instance.store)
        instance.sales_rep = validated_data.get('sales_rep', instance.sales_rep)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.payment_terms = validated_data.get('payment_terms', instance.payment_terms)
        instance.shipping_address = validated_data.get('shipping_address', instance.shipping_address)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        for item in order_items_data:
            order_item = order_items.pop(0)
            order_item.product = item.get('product', order_item.product)
            order_item.quantity = item.get('quantity', order_item.quantity)
            order_item.save()
        return instance