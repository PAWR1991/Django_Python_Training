# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='amount',
            field=models.CharField(max_length=255),
        ),
    ]
