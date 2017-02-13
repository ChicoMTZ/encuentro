# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.conf import settings
from django.utils.text import slugify
from django.contrib.sites.models import Site


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
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def __str__(self):
        return self.name


class Topic(Model):

    user = ForeignKey(User, on_delete=CASCADE, related_name='topic_user', verbose_name=_('Usuario'))
    name = CharField(max_length=45, verbose_name=_('Nombre'))
    description = TextField(verbose_name=_('Descripción'))
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar')
    date_created = DateTimeField(verbose_name=_('Fecha de Creado'), auto_now_add=True)
    sites = ForeignKey(Site, on_delete=CASCADE, related_name='topic_user', verbose_name=_('Sitios'))

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
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def __str__(self):
        return self.speech_type.name + ' de ' + self.topic.name

    def cantidad_de_likes(self):
        likes = self.profile_speech_likes.all()
        return likes.count()


class SpeechResource(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='speechs_resource_user', verbose_name=_('Usuario'))
    speech = ForeignKey(Speech, related_name='recursos')
    recurso = FileField(upload_to='recursos/')
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def nombre(self):
        direccion = self.recurso.name
        nombre = direccion.split('/').pop()
        return nombre

    def get_absolute_url(self):
        return '/activity/' + self.speech.topic.slug + "/" + self.speech.slug


class Forum_User_Profile(Model):

    gender_choice = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino')
    )

    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Usuario'))
    name = CharField(max_length=255, verbose_name=_('Nombre'), blank=True)
    last_name = CharField(max_length=255, verbose_name=_('Apellido'), blank=True)
    institution = CharField(max_length=12, verbose_name=_('Institución'), blank=True)
    alimentary_restriction = TextField(verbose_name=_('Restrinción Alimentaria'), null=True)
    born_date = DateField(verbose_name=_('Fecha de Nacimiento'), null=True)
    gender = CharField(max_length=9, choices=gender_choice, verbose_name=_('Genero'), blank=True)
    health_consideration = TextField(verbose_name=_('Condiciones de Salud'), null=True)
    identification = CharField(max_length=12, verbose_name=_('Identificación'), null=True)
    nationality = CharField(max_length=12, verbose_name=_('Nacionalidad'), blank=True)
    snore = BooleanField(verbose_name=_('¿Ronca?'), default=False, blank=True)
    enrolled = BooleanField(verbose_name=_('¿Matriculado?'), default=False, blank=True)
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    # About the likes and the register in the differents activities
    likes = ManyToManyField(Speech, related_name='profile_speech_likes', blank=True)
    matriculatedspeechs = ManyToManyField(Speech, blank=True)
    entry_country = IntegerField(verbose_name=_('Entradas del País'), null=True)
    out_country = IntegerField(verbose_name=_('Salidas del País'), null=True)
    entry_port = CharField(max_length=100, verbose_name=_('Puerto de Entrada'), null=True)
    out_port = CharField(max_length=100, verbose_name=_('Puerto de Salida'), null=True)
    entry_country_date = DateField(verbose_name=_('Fecha de Entrada al país'), null=True)
    out_country_date = DateField(verbose_name=_('Fecha de Salida del país'), null=True)
    letter = TextField(verbose_name=_('Carta Migratoria'), null=True)
    invitation_file = BooleanField(verbose_name=_('¿Email de Invitación?'), default=False)
    diploma = BooleanField(verbose_name=_('¿Email de Diploma?'), default=False)
