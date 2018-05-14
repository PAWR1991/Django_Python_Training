# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .. LaR_app.models import *
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
	if "user_id" not in request.session:
		return redirect("/")
	context = {
		"user": User.objects.get(id=request.session["user_id"]),
		# "users": User.objects.all().exclude(id=request.session["user_id"]),
		# "your_messages":Message.objects.filter(received_by=request.session["user_id"])
	}

	return render(request,"books_app/home.html", context)

def addpage(request):
	return render(request,"books_app/addpage.html")

def addbook(request):
	# print request.POST
	# print len(request.POST["author"])
	context={
		"user":User.objects.get(id=request.session["user_id"]),
		"author":None,
		"book":None,
		"review":None
	}

	if len(request.POST["author"]) > 1:
		context["author"] = Author.objects.create(name=request.POST["author"])
		context["book"] =Book.objects.create(
			title=request.POST["title"],
			author=context["author"]
		)
		print context["user"]
		context["review"] = Review.objects.create(
			desc=request.POST["desc"],
			rating=request.POST["rating"],
			book=context["book"],
			users=context["user"]
		)
		# context["review"].users.add(context["user"])
		print context["review"].users.all()
	# else:
	# 	Author.objects.filter(name=request.POST["list"])
	request.session["book_id"]=context["book"].id
	return redirect("/books/" + str(request.session["book_id"]))

def bookspage(request, id):
	context={
		"user":User.objects.get(id=request.session["user_id"]),
		"book":Book.objects.get(id=request.session["book_id"]),
		"author":None,
		"reviews":None
	}
	context["author"]=Author.objects.get(id=context["book"].author.id)
	context["reviews"]=Review.objects.filter(book=id)

	return render(request,"books_app/bookspage.html", context)
