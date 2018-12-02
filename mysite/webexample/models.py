# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Schedule (models.Model):
    name = models.CharField(max_length = 30);
    para1= models.TextField();
    para2 = models.TextField();
    para3 = models.TextField();
    para4 = models.TextField();

    def __unicode__(self):
        return self.name
