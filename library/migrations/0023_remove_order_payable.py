# Generated by Django 4.1 on 2023-01-30 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0022_delete_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payable',
        ),
    ]