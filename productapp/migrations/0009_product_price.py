# Generated by Django 5.2.3 on 2025-07-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0008_productvariant_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
