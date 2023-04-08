from rest_framework import serializers
from api.models import Pharmacy, ReportingManager, Doctor, SalesRepresentative, Store, Distributor, Product, Order, OrderItem, Inventory

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'
        
class ReportingManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingManager
        fields = '__all__'

class SalesRepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRepresentative
        fields = ['id', 'name', 'email', 'password']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

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
    # order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    # def create(self, validated_data):
    #     order_items_data = validated_data.pop('order_items')
    #     order = Order.objects.create(**validated_data)
    #     for item in order_items_data:
    #         OrderItem.objects.create(order=order, **item)
    #     return order

    # def update(self, instance, validated_data):
    #     order_items_data = validated_data.pop('order_items')
    #     order_items = (instance.order_items).all()
    #     order_items = list(order_items)
    #     # instance.store = validated_data.get('store', instance.store)
    #     instance.pharmacy = validated_data.get('pharmacy', instance.pharmacy)
    #     instance.product_name = validated_data.get('product_name', instance.product_name)
    #     instance.sales_rep = validated_data.get('sales_rep', instance.sales_rep)
    #     instance.order_image = validated_data.get('order_image', instance.order_book_image)
    #     instance.distributer = validated_data.get('distributer', instance.distributer)
    #     instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
    #     # instance.payment_terms = validated_data.get('payment_terms', instance.payment_terms)
    #     instance.shipping_address = validated_data.get('shipping_address', instance.shipping_address)
    #     # instance.notes = validated_data.get('notes', instance.notes)
    #     instance.order_date = validated_data.get('order_date',instance.order_date)
    #     instance.save()
    #     for item in order_items_data:
    #         order_item = order_items.pop(0)
    #         order_item.product = item.get('product', order_item.product)
    #         order_item.quantity = item.get('quantity', order_item.quantity)
    #         order_item.save()
    #     return instance