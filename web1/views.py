from django.shortcuts import render
from django.contrib.sites.models import Site
# Create your views here.
from registration.backends.hmac.views import RegistrationView
from django.core.urlresolvers import set_urlconf, get_urlconf
from registration.forms import *
from registration import signals
from web1.forms import ProfileForm
from web1.models import Profile
from django.conf import settings


def inicio(request):

    pass


def index(request):
    settings.ALLOWED_HOSTS.append('pp.localhost', )
    currentSite = Site.objects.get_current()
    if currentSite.domain != request.get_host():
        set_urlconf("sitios.default")
        request.urlconf = "sitios.default"
        print request.get_host()
        print currentSite
        return render(request, 'home_sites.html')
    else:

        return render(request, 'home.html')


def crear(request):
    print request.get_host()
    return render(request, 'unico.html')


class createProfile(RegistrationView):

    template_name = 'usuarios/create_profile.html'

    def register(self, form):
        formuser = RegistrationForm(data={'username': form.cleaned_data["username"], 'email': form.cleaned_data["email"], 'password1': form.cleaned_data["password1"],
                                          'password2': form.cleaned_data["password2"]})
        new_user = self.create_inactive_user(formuser)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)

        return new_user