# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-13 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20171013_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='trial_length',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
