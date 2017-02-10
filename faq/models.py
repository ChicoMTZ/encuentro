# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import *
from web1.models import Eventos
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class CategoriaPregunta(Model):
    emoji_alt = CharField(verbose_name=_('Emoji'), max_length=50)
    nombre = CharField(max_length=100, verbose_name=_('Categoría'))

    def __str__(self):
        return self.nombre


class Pregunta(Model):
    categoria = ForeignKey(CategoriaPregunta, verbose_name=_('Categoria'), on_delete=CASCADE)
    respuesta = TextField(verbose_name=_('Respuestas'))
    fechaCreacion = DateField(verbose_name=_('Fecha de Creación'), auto_now_add=True)
    publicada = BooleanField(verbose_name=_('Publicado'))
    pregunta = TextField(verbose_name=_('Pregunta'))
    sites = OneToOneField(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def __str__(self):
        return self.pregunta


