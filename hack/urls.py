"""hack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from firstaid.views import firstaid,firstaid_display,firstaid_feed
from drugdict.views import drugdict,drug_display,drug_feed
from core.views import home
from search.views import search

urlpatterns = [
    url(r'^admin/', admin.site.urls),

#home urls
    url(r'^home/$',home,name='home'),

#first_aid urls
    url(r'^firstaid/$',firstaid,name='firstaid'),
    url(r'^firstaid_display/(?P<id>[0-9].*)/$',firstaid_display,name='firstaid_display'),
    url(r'^firstaidfeed/$',firstaid_feed,name='firstaid_feed'),

#drug_dictionary urls
    url(r'^drugdict/$',drugdict,name='drugdict'),    
    url(r'^drugdisplay/(?P<id>[0-9].*)/$',drug_display,name='drugdisplay'),
    url(r'^drugfeed/$',drug_feed,name='drugfeed'),

#search urls
    url(r'^search/$',search, name='search'),

]

from django.conf import settings
from django.views.static import serve

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root':settings.MEDIA_ROOT})
]