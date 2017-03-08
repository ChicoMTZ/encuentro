# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import *
from faq.models import *
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404

class Faq(ListView):
    template_name = 'faq/faq.html'
    context_object_name = 'faq_list'

    def get_queryset(self):
        return Pregunta.objects.filter(publicada=True, sites=get_current_site(self.request)).order_by('-fechaCreacion')

    def get(self, request, *arg, **kwargs):
        if get_current_site(request).domain == 'localhost:8000':
            raise Http404
        return super(Faq, self).get(request, *arg, **kwargs)
