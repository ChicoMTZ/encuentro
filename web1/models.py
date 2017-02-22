# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class Profile(Model):

    user = OneToOneField(User, on_delete=CASCADE, verbose_name=_('Usuario'))
    event_url = CharField(max_length=255, verbose_name=_('Nombre Evento'))

    def __str__(self):
        return self.user.username


class pagina_web(Model):
    logo = ImageField(verbose_name=_('logo'), upload_to='paginas/logos/')
    banner = ImageField(verbose_name=_('banner'), upload_to='paginas/banner/')


class Patrocinadores(Model):
    name = CharField(max_length=100, verbose_name=_('Nombre'))
    web = URLField(verbose_name=_('Web'))
    logo = ImageField(verbose_name=_('logo'), upload_to='logos/')


class enlaces(Model):
    redes = (
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter')
    )
    red_social = CharField(max_length=8, verbose_name=_('Red social'), choices=redes)
    direccion = URLField(verbose_name=_('Direccion'))
