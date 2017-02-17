from django.contrib import admin
from actividades.models import *
# Register your models here.


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TopicAdmin, self).get_queryset(request)
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
