from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from becas.models import Inscription
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404

@method_decorator(login_required, name='dispatch')
class becas(CreateView, SuccessMessageMixin):
    template_name = 'becas/becas.html'
    context_object_name = 'becas'
    success_url = '/'
    fields = ['mozilla_subvention_description']
    success_message = 'Tu propuesta ha sido enviada. Necesita la aprobacion de un administrador'

    def form_valid(self, form):
        form.instance.subvention_request = True
        form.instance.user = self.request.user
        form.instance.preregistered = True
        form.instance.sites = get_current_site(self.request)

        return super(becas, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not Inscription.objects.filter(user=self.request.user, sites=get_current_site(self.request)):
            return super(becas, self).dispatch(request, *args, **kwargs)

        estado = Inscription.objects.get(user=self.request.user, sites=get_current_site(self.request))

        if estado.subvention_request and estado.not_registered and estado.registered:
            return render(self.request, 'becas/becas.html', {'estado': 'Analizando'})
        elif estado.subvention_request and estado.not_registered == False and estado.registered:
            return render(self.request, 'becas/becas.html', {'estado': 'Ha sido Aprobado'})

        elif estado.subvention_request and estado.not_registered and estado.registered == False:
            return render(self.request, 'becas/becas.html', {'estado': 'Denegado'})
        elif estado.subvention_request and estado.not_registered == False and estado.registered == False:
            return render(self.request, 'becas/becas.html', {'estado': 'Analizando'})

    def get_queryset(self):
        return Inscription.objects.filter(sites=get_current_site(self.request))

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(becas, self).get(request, *arg, **kwargs)
