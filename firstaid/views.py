# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.genric import ListView,DetailView
from django.http import HttpResponse
from django.views import 
from .forms import UploadForm
from .models import Upload

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def firstaid(request):
	
	form=UploadForm()
	if request.method=='POST':
		form=UploadForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Form submission successful')
	context={
		'form':form,
	}
	return render(request,'firstaid_update.html',context)

def firstaid_display(request,id):
	context={
		'data':Upload.objects.get(id=id)
	}
	return render(request,'firstaid_display.html',context)



def firstaid_feed(request):
    data_list = Upload.objects.all()
    paginator = Paginator(data_list, 5)

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data= paginator.page(paginator.num_pages)

    return render(request, 'firstaid_feed.html', {'data': data})