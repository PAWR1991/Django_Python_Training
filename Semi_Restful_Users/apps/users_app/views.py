# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def users(request):
	return render(request, 'users_app/users.html')
