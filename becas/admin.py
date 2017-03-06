from django.contrib import admin
from becas.models import Inscription
from web1.admin import admin_site
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail


class Inscription_Admin(admin.ModelAdmin):
    exclude = ('sites', 'user')
    list_display = ('user', 'subvention_request', 'registered', 'not_registered')
    list_editable = ('registered', 'not_registered')
    actions = ['send_email_aprove', 'send_email_denieg']

    def get_queryset(self, request):
        qs = super(Inscription_Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sites=get_current_site(request))

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.sites = get_current_site(request)
        obj.save()

    def send_email_aprove(self, request, queryset):
        for date in queryset:
            send_mail('Hola', 'Usted ha sido aprobado', 'chicomtz.sr@gmail.com', [date.user.email])
        queryset.update(registered=True)
        rows_updated = queryset.update(not_registered=False)

        if rows_updated == 1:
            message_bit = "1 email was sent"
        else:
            message_bit = "%s emails were sent" % rows_updated
        self.message_user(request, "%s successfully" % message_bit)

    send_email_aprove.short_description = 'Enviar correo de aprobado'

    def send_email_denieg(self, request, queryset):
        for date in queryset:
            send_mail('Hola', 'Ha sido denegado', 'chicomtz.sr@gmail.com', [date.user.email])

        queryset.update(not_registered=True)
        rows_updated = queryset.update(registered=False)

        if rows_updated == 1:
            message_bit = "1 email was sent"
        else:
            message_bit = "%s emails were sent" % rows_updated
        self.message_user(request, "%s successfully" % message_bit)


    send_email_denieg.short_description = 'Enviar correo de no aprobado'

admin_site.register(Inscription, Inscription_Admin)
