# Generated by Django 5.0.1 on 2024-03-19 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='image')),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
