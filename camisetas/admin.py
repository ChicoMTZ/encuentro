from django.contrib import admin
from camisetas.models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from web1.admin import admin_site


class TshirtAdmin(admin.ModelAdmin):
    exclude = ('user', 'sites')

    def get_queryset(self, request):
        qs = super(TshirtAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(evento__sitio=get_current_site(request))

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sites = get_current_site(request)
        obj.save()


class TshirtStyleAdmin(admin.ModelAdmin):
    exclude = ('user', 'sites')

    def get_queryset(self, request):
        qs = super(TshirtStyleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(evento__sitio=get_current_site(request))

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sites = get_current_site(request)
        obj.save()

admin_site.register(Tshirt, TshirtAdmin)
admin_site.register(TshirtStyle, TshirtAdmin)
