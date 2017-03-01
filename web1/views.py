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
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


def index(request):
    if get_current_site(request).domain != 'localhost:8000':
        return render(request, 'sitios_web/home_sites.html', {'sitios': WebBuilder.objects.filter(sites=get_current_site(request))})
    else:
        return render(request, 'plataforma/home.html')


def CreargruposPermisos():
    # Estableciendo Grupos y Permisos
    new_group, created = Group.objects.get_or_create(name='Sitios_Admin')
    ct = ContentType.objects.get_for_model(WebBuilder)
    AddWebBuilder = Permission.objects.get(codename='can_add_WebBuilder',
                                           name='Can add Web Builder',
                                           content_type=ct)
    ChangeWebBuilder = Permission.objects.get(codename='can_change_WebBuilder',
                                              name='Can change Web Builder',
                                              content_type=ct)
    DeleteWebBuilder = Permission.objects.get(codename='can_delete_WebBuilder',
                                              name='Can delete Web Builder',
                                              content_type=ct)
    new_group.permissions.add(AddWebBuilder)
    new_group.permissions.add(ChangeWebBuilder)
    new_group.permissions.add(DeleteWebBuilder)
