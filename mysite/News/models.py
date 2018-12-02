# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
# coding=utf8
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30);
    birthdata = models.DateField();
    number = models.CharField(max_length = 20);
    email = models.EmailField();

    def __unicode__(self):
        return self.name
