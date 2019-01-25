# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(u'标题', max_length=255)
    content = models.TextField(u'内容', null=True)
