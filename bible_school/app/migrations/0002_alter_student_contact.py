# Generated by Django 3.2.7 on 2021-09-13 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
