# Generated by Django 5.1.5 on 2025-01-15 20:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Product ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Product Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Product Price Per Hour')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('name', '-created_at'),
            },
        ),
    ]
