# Generated by Django 4.1 on 2023-01-13 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0016_alter_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=150)),
                ('division', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=30)),
                ('payment_method', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=20)),
                ('transaction_id', models.IntegerField()),
                ('payable', models.IntegerField()),
                ('totalbook', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
