# Generated by Django 4.2.2 on 2023-06-23 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product_selectedcolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='selectedColor',
        ),
    ]
