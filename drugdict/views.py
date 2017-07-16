# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .forms import DrugForm
from .models import UploadDrug

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def drugdict(request):
	stdlogger.info("Entering drugdictionary")
	form=DrugForm()
	if request.form=='POST':
		form=DrugForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success('Drug is completed succesfuly')
		details={'form':form}
		
		return render(request,'Drug_update.html',details)


def drug_display(request,id):
	context={
	'data':UploadDrug.objects.get(id=id)
	}
	return render(request,'drug_display.html',context)


def drug_feed(request):
    data_list = UploadDrug.objects.all()
    paginator = Paginator(data_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data= paginator.page(paginator.num_pages)

    return render(request, 'drug_feed.html', {'data': data})


