from django.contrib import admin
from web1.admin import admin_site
from actividades.models import *
from django.contrib.sites.shortcuts import get_current_site


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


class TopicAdmin(admin.ModelAdmin):
    exclude = ('user', 'slug', 'sites')

    def get_queryset(self, request):
        qs = super(TopicAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sites=get_current_site(request))

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.slug = slugify(get_current_site(request).name + ' ' + obj.name)
        obj.sites = get_current_site(request)
        obj.save()


admin_site.register(Forum_User_Profile, SpeechAdmin)
admin_site.register(Speech, SpeechAdmin)
admin_site.register(SpeechType, TopicAdmin)
admin_site.register(SpeechResource, SpeechAdmin)
admin_site.register(Topic, TopicAdmin)