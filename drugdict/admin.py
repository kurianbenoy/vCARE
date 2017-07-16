# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UploadDrug

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pillname']}),
        ('Date information', {'fields': ['sideeffects']}),
    ]

admin.site.register(UploadDrug, QuestionAdmin)
