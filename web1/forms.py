from registration.forms import *
from web1.models import *
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist


class Form_Admin(AuthenticationForm):
    def confirm_login_allowed(self, user):

        if user.is_superuser:
            return super(Form_Admin, self).confirm_login_allowed(user)
        try:
            pp = Eventos.objects.get(perfil__user=user)
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                _("Your user don't have any event created"),
                code='inactive',)

        if get_current_site(self.request).domain != pp.sites.domain:

            raise forms.ValidationError(
                _("You are not allowed to this domain."),
                code='inactive',
            )
