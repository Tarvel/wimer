# Generated by Django 5.2.3 on 2025-07-04 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0009_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='base_price',
        ),
    ]
