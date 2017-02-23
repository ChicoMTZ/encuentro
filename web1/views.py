from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.sites.models import Site
from registration.backends.hmac.views import RegistrationView
from django.core.urlresolvers import set_urlconf, get_urlconf
from registration.forms import *
from registration import signals
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site

from web1.models import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm


def index(request):

    if get_current_site(request).domain != 'localhost:8000':
        print get_current_site(request)
        return render(request, 'sitios_web/home_sites.html', {'logo': pagina_web.objects.filter(user=request.user)})


class createUser(RegistrationView):

    template_name = 'usuarios/create_profile.html'

    def register(self, form):
        formuser = RegistrationForm(data={'username': form.cleaned_data["username"], 'email': form.cleaned_data["email"], 'password1': form.cleaned_data["password1"],
                                          'password2': form.cleaned_data["password2"]})
        new_user = self.create_inactive_user(formuser)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        currentSite = Site.objects.get_current()
        if currentSite.domain == self.request.get_host():
            g = Group.objects.get(name='Sitios_Admin')
            g.user_set.add(new_user)
            new_user.is_staff = True
            new_user.save()
        return new_user
