from django.db import models

class SalesRepresentative(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def _str_(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='store_logos')
    sales_rep = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, related_name='stores')

    def _str_(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)

    def _str_(self):
        return self.name


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')
    sales_rep = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, related_name='orders')
    delivery_date = models.DateField()
    payment_terms = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    notes = models.TextField()

    def _str_(self):
        return f"Order for {self.store.name} ({self.delivery_date})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def _str_(self):
        return f"{self.product.name} ({self.quantity})"
