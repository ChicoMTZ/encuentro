# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class Profile(Model):

    gender_choice = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino')
    )
    name = CharField(max_length=20, verbose_name='Nombre')
    LastName = CharField(max_length=50, verbose_name='Apellidos')
    country = CharField(max_length=60, verbose_name='País')
    user = OneToOneField(User, on_delete=CASCADE, verbose_name=_('Usuario'))
    email = EmailField()
    gender = CharField(max_length=9, choices=gender_choice, verbose_name=_('Genero'))
    identification = CharField(max_length=12, verbose_name=_('Identificación'), null=True)

    def __unicode__(self):
        return '%s' % self.user


class Patrocinadores(Model):
    name = CharField(max_length=100, verbose_name=_('Nombre'))
    web = URLField(verbose_name=_('Web'))
    logo = ImageField(verbose_name=_('logo'), upload_to='paginas/patrocinadores/')
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('Usuario'))
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def __unicode__(self):
        return '%s' % self.name


class enlaces(Model):
    redes = (
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter')
    )
    red_social = CharField(max_length=8, verbose_name=_('Red social'), choices=redes)
    direccion = URLField(verbose_name=_('Direccion'))
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('Usuario'))
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def __unicode__(self):
        return '%s' % self.sites


class WebBuilder (Model):
    # Pagina Web
    WebLogo = ImageField(verbose_name=_('Logo'), upload_to='paginas/logos/')
    banner = ImageField(verbose_name=_('Banner'), upload_to='paginas/banner/')
    slogan = CharField(max_length=100, verbose_name=_('Slogan'))
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('Usuario'))
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def __unicode__(self):
        return '%s' % self.sites


class Eventos(Model):
    perfil = ForeignKey(Profile, CASCADE, verbose_name='Perfil')
    event_name = CharField(max_length=255, verbose_name=_('Nombre Evento'))
    date_start = DateField(verbose_name=_('Fecha de inicio'), blank=True)
    date_end = DateField(verbose_name=_('Fecha Final'), blank=True)
    country = CharField(max_length=100, verbose_name=_('País'), blank=True)
    places = CharField(max_length=100, verbose_name=_('Lugar'), blank=True)
    payed = BooleanField(default='False')
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def __unicode__(self):
        return '%s' % self.event_name
