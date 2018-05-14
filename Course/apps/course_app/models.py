# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
	def addCourse(self, post_data):
		errors = []
		if len(post_data["name"]) < 1:
			errors.append("Name is required")
		elif len(post_data["name"]) < 5:
			errors.append("Name must be 5 characters or more")

		if len(post_data["desc"]) < 1:
			errors.append("Description is required")
		elif len(post_data["desc"]) < 15:
			errors.append("Description must be 15 characters or more")

		if len(errors)>0:
			return errors
		else:
			return Course.objects.create(name=post_data["name"], desc=post_data["desc"])

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now=True)
	objects = CourseManager()
		