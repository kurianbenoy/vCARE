# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .forms import MessageForm
from .models import Messages

from django.contrib import messages

# Create your views here.

def home(request):
	print request.POST, request.FILES
	form=MessageForm()
	if request.method=='POST':
		form=MessageForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Message send successful')
	context={
		'form':form,
	}
	return render(request,'home.html',context)