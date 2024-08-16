# Generated by Django 5.0.1 on 2024-03-20 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_add_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
        ),
        migrations.AddField(
            model_name='add_cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
