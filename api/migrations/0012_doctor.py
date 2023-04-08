# Generated by Django 4.1.7 on 2023-04-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_order_product_name_order_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('specialization', models.CharField(max_length=100)),
                ('is_clinic_owner', models.BooleanField(default=False)),
                ('clinic_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('registration_council', models.CharField(max_length=100)),
                ('registration_no', models.CharField(max_length=100)),
                ('yor', models.IntegerField()),
                ('photo_id_proof', models.FileField(upload_to='doctor/id_proof')),
                ('registration_proof', models.FileField(upload_to='doctor/registration_proof')),
                ('clinic_registration_proof', models.FileField(upload_to='doctor/clinic_reg_proof')),
            ],
        ),
    ]