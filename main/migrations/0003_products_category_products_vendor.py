# Generated by Django 4.2.3 on 2023-08-05 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_productcategory_products_alter_vendor_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productcategory', to='main.productcategory'),
        ),
        migrations.AddField(
            model_name='products',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productvendor', to='main.vendor'),
        ),
    ]