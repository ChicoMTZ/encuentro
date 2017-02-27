from registration.forms import *
from web1.models import *
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site


class Form_Admin(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pp = Eventos.objects.get(perfil__user=user)

        if get_current_site(self.request).domain != pp.sites.domain:

            raise forms.ValidationError(
                _("You are not allowed to this domain."),
                code='inactive',
            )
