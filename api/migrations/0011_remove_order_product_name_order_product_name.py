# Generated by Django 4.1.7 on 2023-04-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_order_product_name_order_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_name',
        ),
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.ManyToManyField(to='api.product'),
        ),
    ]