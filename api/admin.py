from django.contrib import admin
from api.models import Pharmacy, ReportingManager, SalesRepresentative, Doctor, Store, Product, Distributor, Order, OrderItem

@admin.register

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(ReportingManager)
class ReportingManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(SalesRepresentative)
class SalesRepresentativeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone_number', 'email', 'sales_rep')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category')

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('name','location','master_d', 'category')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'pharmacy', 'sales_rep', 'delivery_date', 'shipping_address')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
