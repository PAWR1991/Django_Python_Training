# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
	"""docstring for Dojos"""
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	def __repr__(self):
		return "Name: {} city: {} state:{}".format(self.name, self.city, self.state)

class Ninja(models.Model):
	"""docstring for Ninja"""
	dojo = models.ForeignKey(Dojo, related_name="ninjas")
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)

	def __repr__(self):
		return "Dojo: {} Name: {} {} ".format(self.dojo, self.first_name, self.last_name)

