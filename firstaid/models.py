# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Upload(models.Model):
	situations= models.CharField(max_length=20)
	guidelines=models.TextField()
	treatment=models.TextField()

	def __unicode__(self):
		return self.situations