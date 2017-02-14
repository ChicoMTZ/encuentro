from django.contrib import admin
from django.contrib.admin import site, AdminSite
from .models import *
from actividades.models import *
from becas.models import Inscription
from camisetas.models import Tshirt, TshirtStyle
from faq.models import *
from django.utils.text import slugify
from django.contrib.sites.shortcuts import get_current_site
from web1.forms import Form_Admin


class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'
    login_form = Form_Admin

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Eventos)

for model_cls, admin_obj in list(site._registry.items()):
     admin_site.register(model_cls, type(admin_obj))


class Pagina_web_Admin(admin.ModelAdmin):
    exclude = ('user', 'sites')

    def get_queryset(self, request):
        qs = super(Pagina_web_Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sites=get_current_site(request))

    def save_model(self, request, obj, form, change):
        obj.sites = get_current_site(request)
        obj.user = request.user
        obj.save()


class ProfileAdmin(admin.ModelAdmin):
    exclude = ('sites', 'user')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sites = get_current_site(request)
        obj.save()

    def get_queryset(self, request):
        qs = super(ProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sites=get_current_site(request))


class SpeechAdmin(admin.ModelAdmin):
    exclude = ('sites', 'user')

    def get_queryset(self, request):

        qs = super(SpeechAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sites=get_current_site(request))

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sites = get_current_site(request)
        obj.save()


admin_site.register(Profile, ProfileAdmin)
admin_site.register(WebBuilder, Pagina_web_Admin)
admin_site.register(Patrocinadores, Pagina_web_Admin)
