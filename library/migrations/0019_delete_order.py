# Generated by Django 4.1 on 2023-01-16 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_remove_order_district_remove_order_division_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
