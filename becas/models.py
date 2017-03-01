# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models import *
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class Inscription(Model):
    user = OneToOneField(User, on_delete=CASCADE, verbose_name=_('Usuario'))
    mozilla_subvention_description = TextField(verbose_name=_('Mozilla Descripción Propuesta'))
    payed = BooleanField(verbose_name=_('¿Pagado?'), default=False)
    not_registered = BooleanField(verbose_name=_('No aprobado'), default=False)
    registered = BooleanField(verbose_name=_('Aprobado'), default=False)
    subvention_request = BooleanField(verbose_name=_('¿Propuesta Enviada?'), default=False)
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def __str__(self):
        return self.user.username
