# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import *
from faq.models import *


class Faq(ListView):
    template_name = 'faq/faq.html'
    queryset = Pregunta.objects.filter(publicada=True).order_by('-fechaCreacion')
    context_object_name = 'faq_list'