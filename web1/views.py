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
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm


def index(request):

    currentSite = Site.objects.get_current()

    if currentSite.domain != request.get_host():

        return render(request, 'sitios_web/home_sites.html')
    else:
        return render(request, 'plataforma/home.html')



