from django.contrib import admin
from .models import *
from .models import Profile
from actividades.models import *
from django.utils.text import slugify
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site


@admin.register(Topic)
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


@admin.register(pagina_web, centro, Patrocinadores, enlaces)
class Pagina_web_Admin(admin.ModelAdmin):
    exclude = ('user', 'sites')

    def get_queryset(self, request):
        qs = super(Pagina_web_Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sites = get_current_site(request)
        obj.save()


@admin.register(SpeechType)
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


@admin.register(Profile)
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


@admin.register(Speech, SpeechResource, Forum_User_Profile)
class SpeechAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(SpeechAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)