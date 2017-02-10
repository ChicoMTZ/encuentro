# -*- coding: UTF-8 -*-
from web1.models import Patrocinadores
from camisetas.models import Tshirt
from django.contrib.sites.shortcuts import get_current_site


def url(request):

    value = {'url': request.path}
    return value


def patrocinadores(request):

    value = {'imagen': Patrocinadores.objects.filter(sites=get_current_site(request))}
    return value


def camisetas(request):
    user = request.user
    if not user.is_anonymous:
        value = {'pedidos': Tshirt.objects.filter(user=user, style__sites=get_current_site(request))}
        return value
    else:
        value = ''
        return value


