# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
# from .models import User
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
	recipes = [r for r in Recipe.objects.all()]
	recipes = sorted(recipes, key=lambda recipe: -len(recipe.likes.all()))
	current_user=User.objects.get(id=request.session["user_id"])
	# recipes = Recipe.objects.all().order_by('-likes')
	return render(request,'recipe_app/index.html',{"user":current_user, "recipes":recipes} )

def recipe(request):
	response_tuple = Recipe.objects.addRecipe(request.POST, request.session["user_id"])
	if not response_tuple[0]:
		for error in response_tuple[1]:
			messages.add_message(request, messages.ERROR, error)
	return redirect('/dashboard')

def like(request, recipe_id):
	liked_recipe = Recipe.objects.get(id=recipe_id)
	current_user = User.objects.get(id=request.session["user_id"])
	liked_recipe.likes.add(current_user)
	return redirect('/dashboard')