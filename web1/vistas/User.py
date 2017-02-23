# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
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
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.utils.decorators import method_decorator
from actividades.forms import *
from django.contrib import messages
from django.contrib.sites.models import Site
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout
from web1.forms import ProfileForm

@method_decorator(login_required, name='dispatch')
class view_profile(DetailView):
    template_name = 'usuarios/view_profile.html'
    model = Profile


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


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'usuarios/my_edit_profile.html'
    success_url = "/"
    model = Profile


def completarRegistro(request, next):
    return redirect('edit_profile', request.user.profile.pk)


def salir(request):
    return logout(request, next_page='index')