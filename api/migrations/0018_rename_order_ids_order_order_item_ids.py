# Generated by Django 4.1.7 on 2023-04-25 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_order_order_ids'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_ids',
            new_name='order_item_ids',
        ),
    ]