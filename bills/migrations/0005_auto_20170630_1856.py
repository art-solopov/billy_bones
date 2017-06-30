# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-30 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('bills', '0004_bill_state_i'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='printed',
        ),
        migrations.AlterField(
            model_name='bill',
            name='paid',
            field=models.DateField(blank=True, null=True),
        ),
    ]
