# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.sites.models import Site
from registration.backends.hmac.views import RegistrationView
from registration.signals import user_registered
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from web1.models import *
from django.contrib import messages
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.sites.models import Site
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout
from actividades.forms import ProfileForm, EventoForm
from registration.forms import *
from django.utils.text import slugify


@method_decorator(login_required, name='dispatch')
class view_profile(DetailView):
    template_name = 'usuarios/view_profile.html'
    model = Profile


class createUser(RegistrationView):
    template_name = 'usuarios/create_user.html'

    def register(self, form):
        formuser = RegistrationForm(data={'username': form.cleaned_data["username"], 'email': form.cleaned_data["email"], 'password1': form.cleaned_data["password1"],
                                          'password2': form.cleaned_data["password2"]})
        new_user = self.create_inactive_user(formuser)
        user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)

        if get_current_site(self.request).domain == 'localhost:8000':
            grupo = Group.objects.get(name='Sitios_Admin')
            grupo.user_set.add(new_user)
            new_user.is_staff = True
            new_user.save()

        return new_user


@method_decorator(login_required, name='dispatch')
class createProfile(SuccessMessageMixin, CreateView):
    template_name = 'usuarios/create_profile.html'
    model = Profile
    success_url = '/'
    form_class = ProfileForm
    success_message = "El perfil fue creado con éxito"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email

        return super(createProfile, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class createEvent(SuccessMessageMixin, CreateView):
    template_name = 'usuarios/create_event.html'
    model = Eventos
    success_url = '/'
    form_class = EventoForm
    success_message = "Su evento fue creado con éxito"

    def form_valid(self, form):
        form.instance.perfil = self.request.user.profile
        form.instance.sites = Site.objects.create(domain=slugify(form.instance.event_name) + '.' +
                                                                 get_current_site(self.request).domain,
                                                  name=form.instance.event_name)

        return super(createEvent, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'usuarios/my_edit_profile.html'
    success_url = "/"
    model = Profile
    form_class = ProfileForm
    success_message = "Su perfil fue modificado con éxito"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileUpdateView, self).form_valid(form)


@login_required
def salir(request):
    return logout(request, next_page='index')