# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User, Message
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'LaR_app/index.html')

def register(request):

	response = User.objects.register(request.POST)
	
	if response["valid"]:
		request.session["user_id"]=response["user"].id
		return redirect('/home')
	else:
		for error in response["errors"]:
			messages.add_message(request, messages.ERROR, error)
	
		return redirect('/')

def login(request):
	response = User.objects.login(request.POST)

	if response["valid"]:
		request.session["user_id"]=response["user"].id
		return redirect('/home')
	else:
		for error in response["errors"]:
			messages.add_message(request, messages.ERROR, error)

		return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')

def home(request):
	if "user_id" not in request.session:
		return redirect("/")
	context = {
		"user": User.objects.get(id=request.session["user_id"]),
		"users": User.objects.all().exclude(id=request.session["user_id"]),
		"your_messages":Message.objects.filter(received_by=request.session["user_id"])
	}

	return render(request,"LaR_app/home.html", context)

def new_message(request, id):
	
	return render(request, 'LaR_app/new_message.html', {"id":id})

def add_message(request, id):
	new_message = Message.objects.sendMessage( 
		request.POST["content"],
		request.session["user_id"],
		id
	)
	if type(new_message) is unicode:
		messages.add_message(request, messages.ERROR, new_message)
		return redirect("/message/" + str(id))
	else:
		return redirect("/home")

def view_message(request):
	your_messages = Message.objects.filter(received_by=request.session["user_id"])
	return render(request,'LaR_app/view_message.html', {"your_messages":your_messages})