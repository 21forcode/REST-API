# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class poat(models.Model):
	bank_name=models.CharField(default="BANK NAME HERE",max_length=200)
	city=models.CharField(default="BANK city HERE",max_length=200)
	details=models.TextField(default="DETAILS OF BANK GOES HERE")
	def __str__(self):
		return "{} - {}".format(self.bank_name, self.city,self.details)

