from django.contrib import admin
from camisetas.models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

@admin.register(Tshirt)
class TshirtAdmin(admin.ModelAdmin):
    list_display = ('style','user', 'amount', 'size', 'pagada')
    list_display_links = ('style',)
    list_editable = ('amount', 'size', 'pagada')


@admin.register(TshirtStyle)
class TshirtStyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'img1', 'img2', 'img3',)
    list_editable = ('img1', 'img2', 'img3',)
    list_display_links = ('name',)

    def get_queryset(self, request):
        qs = super(TshirtStyleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(evento__sitio=get_current_site(request))

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sites = get_current_site(request)
        obj.save()
