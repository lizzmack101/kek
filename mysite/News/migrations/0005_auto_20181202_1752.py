# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-02 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(max_length=30),
        ),
    ]