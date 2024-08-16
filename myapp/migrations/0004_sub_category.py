# Generated by Django 5.0.1 on 2024-02-16 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_main_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.main_category')),
            ],
        ),
    ]