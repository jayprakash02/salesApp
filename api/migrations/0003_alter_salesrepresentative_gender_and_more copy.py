# Generated by Django 4.1.7 on 2023-04-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_reportingmanager_salesrepresentative_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesrepresentative',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='salesrepresentative',
            name='mylab_id',
            field=models.IntegerField(unique=True),
        ),
    ]