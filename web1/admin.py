from django.contrib import admin
from .models import Profile
from actividades.models import *
from django.utils.text import slugify
from django.contrib.sites.models import Site


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    exclude = ('user', 'slug')

    def get_queryset(self, request):
        qs = super(TopicAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.slug = slugify(Site.objects.get_current().name + ' ' + obj.name)
        obj.save()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(SpeechType)
class SpeechTypeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(SpeechTypeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(SpeechAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(SpeechResource)
class SpeechResourceAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(SpeechResourceAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Forum_User_Profile)
class Forum_User_ProfileAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(Forum_User_ProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
