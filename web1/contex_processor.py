# -*- coding: UTF-8 -*-
from web1.models import Patrocinadores
from camisetas.models import Tshirt


def url(request):

    value = {'url': request.path}
    print request.path
    return value


def patrocinadores(request):

    value = {'imagen': Patrocinadores.objects.all()}
    return value


def camisetas(request):
    user = request.user
    if not user.is_anonymous:
        value = {'pedidos': Tshirt.objects.filter(user=user)}
        return value
    else:
        value = ''
        return value


