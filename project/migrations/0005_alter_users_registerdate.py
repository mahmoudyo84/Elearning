# Generated by Django 5.1.4 on 2024-12-22 17:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_customuser_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='RegisterDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]