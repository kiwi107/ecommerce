# Generated by Django 4.2.2 on 2023-06-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_product_feuturedin_product_featuredin'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredin',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='featuredInProduct', to='app.product'),
        ),
    ]