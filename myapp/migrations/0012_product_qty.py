# Generated by Django 5.0.1 on 2024-04-02 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_product_img1_product_img2_product_img3'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
