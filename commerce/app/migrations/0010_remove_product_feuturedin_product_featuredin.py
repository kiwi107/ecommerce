# Generated by Django 4.2.2 on 2023-06-27 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_product_feuturedin_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='feuturedIn',
        ),
        migrations.AddField(
            model_name='product',
            name='featuredIn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featuredIn', to='app.featuredin'),
        ),
    ]
