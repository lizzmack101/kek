# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-02 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0005_auto_20181202_1752'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
