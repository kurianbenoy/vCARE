# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.db.models import Q
from firstaid.models import Upload

# Create your views here.

def search(request):
    if 'q' in request.GET:
        querystrings = request.GET.get('q').strip()
        print (querystrings)
        querystring=str(querystrings)
        if len(querystring) == 0:
            return redirect('/search/')

        result = Upload.objects.filter(situations__icontains=querystring)

        return render(request, 'results.html', {
            'results': result,
        })
    else:
        return render(request, 'search.html')