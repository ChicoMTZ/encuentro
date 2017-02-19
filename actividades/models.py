# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.conf import settings


class SpeechType(Model):
    speech_choice = (
        ('Talleres', 'Talleres'),
        ('Charlas', 'Charlas'),
        ('Diálogos', 'Diálogos')
    )

    speech_icons = (
        (settings.STATIC_URL + 'img/talleres.png', 'Talleres'),
        (settings.STATIC_URL + 'img/charlas.png', 'Charlas'),
        (settings.STATIC_URL + 'img/dialogos.png', 'Diálogos')
    )
    user = ForeignKey(User, on_delete=CASCADE, related_name='speechs_type_user', verbose_name=_('Usuario'))
    name = CharField(max_length=45, verbose_name=_('Nombre'), choices=speech_choice)
    icons = CharField(max_length=45, verbose_name=_('Iconos'), choices=speech_icons)
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar')

    def __str__(self):
        return self.name


class Topic(Model):

    user = ForeignKey(User, on_delete=CASCADE, related_name='topic_user', verbose_name=_('Usuario'))
    name = CharField(max_length=45, verbose_name=_('Nombre'),unique=True)
    description = TextField(verbose_name=_('Descripción'))
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar')
    date_created = DateTimeField(verbose_name=_('Fecha de Creado'), auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.slug


class Speech(Model):

    class Meta:
        ordering = ["date_created"]

    speech_audience = (
        ('PG', 'Público General'),
        ('NB', 'Nivel Basico'),
        ('NI', 'Nivel Intermedio'),
        ('NA', 'Nivel Avanzado'),
        ('PRO', 'Profesional'),
    )

    speech_type = ForeignKey(SpeechType, verbose_name=_('Tipo de Actividad'))
    topic = ForeignKey(Topic, verbose_name=_('Tema'))
    user = ForeignKey(User, on_delete=CASCADE, related_name='speechs_user', verbose_name=_('Usuario'))
    audience = CharField(verbose_name=_('Público'), choices=speech_audience, max_length=45)
    description = TextField(verbose_name=_('Descripción'))
    notes = TextField(verbose_name=_('Notas'))
    skill_level = PositiveIntegerField(verbose_name=_('Nivel de Habilidad'))
    speaker_information = TextField(verbose_name=_('Información del Autor'))
    title = CharField(max_length=250, verbose_name=_('Título'))
    places = CharField(max_length=250, verbose_name=_('Lugares'), null=True)
    activity_start = DateTimeField(verbose_name=_('Fecha del Evento'), null=True)
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar', max_length=255)
    date_created = DateTimeField(verbose_name=_('Fecha de Creado'), auto_now_add=True)
    published = BooleanField(verbose_name=_('¿Publicado?'), default=False)

    def __str__(self):
        return self.speech_type.name + ' de ' + self.topic.name

    def cantidad_de_likes(self):
        likes = self.profile_speech_likes.all()
        return likes.count()


class SpeechResource(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='speechs_resource_user', verbose_name=_('Usuario'))
    speech = ForeignKey(Speech, related_name='recursos')
    recurso = FileField(upload_to='recursos/')

    def nombre(self):
        direccion = self.recurso.name
        nombre = direccion.split('/').pop()
        return nombre

    def get_absolute_url(self):
        return '/activity/' + self.speech.topic.slug + "/" + self.speech.slug
