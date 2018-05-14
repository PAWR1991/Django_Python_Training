# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
from .models import *
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z9-9.+_-]+@[a-zA-Z9-9.+_-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def register(self, post_data):

		response={
			"valid":True,
			"errors":[],
			"user":None
		}

		#First Name Check
		if len(post_data["first_name"]) < 1:
			response["errors"].append("First Name is required")
		elif len(post_data["first_name"]) < 2:
			response["errors"].append("First First name most be 2 characters or more")

		#Last Name Check
		if len(post_data["last_name"]) < 1:
			response["errors"].append("Last name is required")
		elif len(post_data["last_name"]) < 2:
			response["errors"].append("Last name most be 2 characters or more")

		#Email Check
		if len(post_data["email"]) < 1:
			response["errors"].append("Email is required")
		elif not EMAIL_REGEX.match(post_data["email"]):
			response["errors"].append("No a valid Email address")
		else:
			email_list=User.objects.filter(email=post_data["email"].lower())
			if len(email_list)>0:
				response["errors"].append("Email already exist")

		#Date of Birth Check
		if len(post_data["dob"]) < 1:
			response["errors"].append("Date of Birth is required")
		else:
			date = datetime.strptime(post_data["dob"],'%Y-%m-%d')
			today = datetime.now()
			if date > today:
				response["errors"].append("Date of Birth most be in the past")

		#Password Check
		if len(post_data["password"]) < 1:
			response["errors"].append("Password is required")
		elif len(post_data["password"]) < 8:
			response["errors"].append("Password most be 8 characters or more")

		#Confirm Password Check
		if len(post_data["confirm"]) < 1:
			response["errors"].append("Confirm Password is required")
		elif post_data["confirm"] != post_data["password"]:
			response["errors"].append("Confirm Password did not match")


		if len(response["errors"])>0:

			response["valid"]=False
		else:
			response["user"]=User.objects.create(
				first_name=post_data["first_name"],
				last_name=post_data["last_name"], 
				email=post_data["email"].lower(),
				dob=date,
				password=bcrypt.hashpw(post_data["password"].encode(), bcrypt.gensalt())
				)
		return response

	def login(self, post_data):
		response={
			"valid":True,
			"errors":[],
			"user":None
		}

		#Email Check
		if len(post_data["email"]) < 1:
			response["errors"].append("Email is required")
		elif not EMAIL_REGEX.match(post_data["email"]):
			response["errors"].append("No a valid Email address")
		else:
			email_list=User.objects.filter(email=post_data["email"].lower())
			print "***************************************S"
			print email_list
			if len(email_list)==0:
				response["errors"].append("Unknown email")

		#Password Check
		if len(post_data["password"]) < 1:
			response["errors"].append("Password is required")
		elif len(post_data["password"]) < 8:
			response["errors"].append("Password most be 8 characters or more")

		if len(response["errors"]) == 0:
			hashed_pw = email_list[0].password
			if bcrypt.checkpw(post_data["password"].encode(),hashed_pw.encode()):
				response["user"]=email_list[0]
				
			else:
				response["errors"].append("Incorrect Password")

		if len(response["errors"]) > 0:
			response["valid"]=False
		
		return response

class MessageManager(models.Manager):
	def sendMessage(self, content, sent_by, received_by):
		if len(content) > 0:
			mail = Message.objects.create(
				content=content,
				sent_by_id=sent_by,
				received_by_id=received_by
			)
			return mail
		else:
			return "Message cannot be blank!"

class User(models.Model):
	"""docstring for User"""
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	dob = models.DateField()
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __repr__(self):
		return "Name: {} {} Email: {} ".format(self.first_name, self.last_name, self.email)


class Message(models.Model):
	content = models.TextField(max_length=1000)
	sent_by = models.ForeignKey(User, related_name="sent_messages")
	received_by = models.ForeignKey(User, related_name="received_messages")
	created_at = models.DateTimeField(auto_now_add=True)
	objects = MessageManager()
		