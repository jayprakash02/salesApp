from django.db import models

class ReportingManager(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SalesRepresentative(models.Model):
    GENDER_CHOICES = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    REPORTING_BIZ_UNIT = (
        ('OTC','OTC'),
        ('IVD','IVD'),
        ('HTP','HTP'),
    )
    ZONES = (
        ('East','East'),
        ('West','West'),
        ('South','South'),
        ('North','North'),
    )
    email = models.EmailField(unique=True)
    mylab_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    address = models.CharField(max_length=100)
    reporting_manager = models.ForeignKey(ReportingManager, on_delete=models.CASCADE)
    reporting_business_unit = models.CharField(max_length=10,choices=REPORTING_BIZ_UNIT)
    zone = models.CharField(max_length=6, choices= ZONES, null=True)

    def __str__(self):
        return self.name
    
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)
    is_clinic_owner = models.BooleanField(default=False) 
    clinic_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    registration_council = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=100)
    yor = models.IntegerField()
    photo_id_proof = models.FileField(upload_to="doctor/id_proof")  
    registration_proof = models.FileField(upload_to="doctor/registration_proof")
    clinic_registration_proof = models.FileField(upload_to="doctor/clinic_reg_proof")


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    TYPES = (
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large','Large'),
    )
    IS_OWNER = (
        ('Yes','Yes'),
        ('No','No'),
    )
    IS_ONLINE_FRIENDLY = (
        ('Yes','Yes'),
        ('No','No'),
    )
    name = models.CharField(max_length=100)
    drug_license_number = models.CharField(max_length=100, null=True)
    p_type = models.CharField(max_length=10, choices=TYPES) 
    location = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    is_owner = models.CharField(max_length=5, choices=IS_OWNER)
    contact_person_designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    is_online_friendly = models.CharField(max_length=4, choices=IS_ONLINE_FRIENDLY)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='store_logos')
    sales_rep = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, related_name='stores')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Distributor(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    master_d = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    # store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE,null=True)
    product_name = models.ManyToManyField(Product)
    sales_rep = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE, related_name='orders')
    order_book_image = models.ImageField(upload_to='order_book_images',null=True)
    distributer = models.ForeignKey(Distributor, on_delete=models.CASCADE,null=True)
    delivery_date = models.DateField()
    # payment_terms = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    # notes = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"Order for {self.pharmacy.name} ({self.delivery_date})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
