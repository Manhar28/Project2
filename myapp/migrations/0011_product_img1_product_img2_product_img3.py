# Generated by Django 5.0.1 on 2024-04-02 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_billing_address_billing_address1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
