# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-13 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20171013_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='modules',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='subscription',
            name='price_per_sq_feet',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='subscription',
            name='renewal_dates',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='signup_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='trial',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='trial_length',
            field=models.PositiveSmallIntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='postal_code',
            field=models.CharField(max_length=6),
        ),
    ]
