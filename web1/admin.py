from django.contrib import admin
from django.contrib.admin import site, AdminSite
from .models import *
from actividades.models import *
from becas.models import Inscription
from camisetas.models import Tshirt, TshirtStyle
from faq.models import *
from django.utils.text import slugify
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.admin import Group, User
from django.views.decorators.cache import never_cache
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.admin.forms import AdminAuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.urls import NoReverseMatch, reverse
from django.http import Http404, HttpResponseRedirect
from web1.forms import Form_Admin


class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'
    login_form = Form_Admin

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Eventos)

for model_cls, admin_obj in list(site._registry.items()):
     admin_site.register(model_cls, type(admin_obj))


class TopicAdmin(admin.ModelAdmin):
    exclude = ('user', 'slug', 'sites')

    def get_queryset(self, request):
        qs = super(TopicAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.slug = slugify(get_current_site(request).name + ' ' + obj.name)
        obj.sites = get_current_site(request)
        obj.save()


class Pagina_web_Admin(admin.ModelAdmin):
    exclude = ('user', 'sites')

    def get_queryset(self, request):
        qs = super(Pagina_web_Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.sites = get_current_site(request)
        obj.save()


class SpeechTypeAdmin(admin.ModelAdmin):
    exclude = ('slug', 'user')
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.slug = slugify(get_current_site(request).name + ' ' + obj.name)
        obj.save()

    def get_queryset(self, request):
        qs = super(SpeechTypeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


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
        return qs.filter(user=request.user)


class SpeechAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(SpeechAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class PatrocinadoresAdmin(admin.ModelAdmin):
    exclude = ('sites',)

    def get_queryset(self, request):
        qs = super(PatrocinadoresAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.sites = get_current_site(request)
        obj.save()


admin_site.register(Profile, ProfileAdmin)
admin_site.register(Speech, SpeechAdmin)
admin_site.register(SpeechType, SpeechTypeAdmin)
admin_site.register(SpeechResource, SpeechAdmin)
admin_site.register(Forum_User_Profile, SpeechAdmin)
admin_site.register(WebBuilder, Pagina_web_Admin)
admin_site.register(Topic, TopicAdmin)
admin_site.register(TshirtStyle)
admin_site.register(Tshirt)
admin_site.register(Inscription)
admin_site.register(CategoriaPregunta)
admin_site.register(Pregunta)
admin_site.register(Patrocinadores, PatrocinadoresAdmin)



