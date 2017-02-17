from django.shortcuts import render
from django.contrib.sites.models import Site
from registration.backends.hmac.views import RegistrationView
from django.core.urlresolvers import set_urlconf, get_urlconf
from registration.forms import *
from registration import signals
from django.conf import settings
from django.contrib.auth.models import Group


def index(request):


    currentSite = Site.objects.get_current()


    if currentSite.domain != request.get_host():
        settings.ALLOWED_HOSTS.append('pp.localhost', )
        set_urlconf("sitios.default")
        request.urlconf = "sitios.default"
        print(get_urlconf())
        return render(request, 'sitios_web/home_sites.html')
    else:
        return render(request, 'plataforma/home.html')


class createProfile(RegistrationView):

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

        return new_user