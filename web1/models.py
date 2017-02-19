# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class Profile(Model):
    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Usuario'))
    name = CharField(max_length=255, verbose_name=_('Nombre'))
    last_name = CharField(max_length=255, verbose_name=_('Apellido'))
    event_url = CharField(max_length=255, verbose_name=_('Nombre Evento'))




