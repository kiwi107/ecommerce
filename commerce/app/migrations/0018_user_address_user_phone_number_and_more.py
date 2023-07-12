# Generated by Django 4.2.2 on 2023-06-29 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_order_color_remove_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='address', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 16, 54, 3, 649416)),
        ),
    ]
