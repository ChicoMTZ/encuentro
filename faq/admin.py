# -*- coding: utf-8 -*-
from django.contrib import admin
from faq.models import *
from web1.admin import admin_site
from django.contrib.sites.shortcuts import get_current_site


class PreguntaAdmin(admin.ModelAdmin):
    exclude = ('sites',)

    def get_queryset(self, request):
        qs = super(PreguntaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sites=get_current_site(request))

    def save_model(self, request, obj, form, change):
        obj.sites = get_current_site(request)
        obj.save()

admin_site.register(CategoriaPregunta, PreguntaAdmin)
admin_site.register(Pregunta, PreguntaAdmin)