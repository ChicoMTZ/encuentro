# -*- coding: utf-8 -*-
from django.contrib import admin
from faq.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site

admin.register(CategoriaPregunta)


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(PreguntaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(evento__sitio=get_current_site(request))

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sites = get_current_site(request)
        obj.save()