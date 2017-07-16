# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Messages(models.Model):
	name= models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	comments=models.TextField()

	def __unicode__(self):
		return self.name
