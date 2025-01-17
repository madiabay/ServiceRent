# Generated by Django 5.1.5 on 2025-01-17 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_products', '0001_initial'),
        ('orders', '0002_alter_order_options'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='orders.order', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_products', to='products.product', verbose_name='Product'),
        ),
    ]
