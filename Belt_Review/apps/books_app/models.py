# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..LaR_app.models import *
from .models import *
# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author, related_name="books")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
	desc = models.TextField()
	rating = models.IntegerField()
	book = models.ForeignKey(Book, related_name="book_reviews")
	users = models.ForeignKey(User, related_name="user_reviews")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		

