# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UploadDrug(models.Model):
	pillname= models.CharField(max_length=20)
	sideeffects=models.TextField()
	warning=models.TextField()
	dosage=models.TextField()

	def __unicode__(self):
		return self.pillname
