# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-13 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='postal_code',
            field=models.PositiveIntegerField(),
        ),
    ]
