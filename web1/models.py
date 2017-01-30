# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import *
from django.utils.translation import ugettext_lazy as _


class Profile(Model):
    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Usuario'))
    name = CharField(max_length=255, verbose_name=_('Nombre'))
    last_name = CharField(max_length=255, verbose_name=_('Apellido'))
    event_url = CharField(max_length=255, verbose_name=_('Nombre Evento'))
    # institution = CharField(max_length=12, verbose_name=_('Institución'))
    # alimentary_restriction = TextField(verbose_name=_('Restrinción Alimentaria'), null=True)
    # born_date = DateField(verbose_name=_('Fecha de Nacimiento'))
    # gender = CharField(max_length=1, choices=gender_choice, verbose_name=_('Genero'))
    # health_consideration = TextField(verbose_name=_('Condiciones de Salud'), null=True)
    # identification = CharField(max_length=12, verbose_name=_('Identificación'), null=True)
    # nationality = CharField(max_length=12, verbose_name=_('Nacionalidad'))
    # snore = BooleanField(verbose_name=_('¿Ronca?'), default=False)
    # enrolled = BooleanField(verbose_name=_('¿Matriculado?'), default=False)
    #
    # About the likes and the register in the differents activities
    # likes = ManyToManyField(Speech, related_name='profile_speech_likes', blank=True)
    # matriculatedspeechs = ManyToManyField(Speech, blank=True)
    # entry_country = IntegerField(verbose_name=_('Entradas del País'), null=True)
    # out_country = IntegerField(verbose_name=_('Salidas del País'), null=True)
    # entry_port = CharField(max_length=100, verbose_name=_('Puerto de Entrada'), null=True)
    # out_port = CharField(max_length=100, verbose_name=_('Puerto de Salida'), null=True)
    # entry_country_date = DateField(verbose_name=_('Fecha de Entrada al país'), null=True)
    # out_country_date = DateField(verbose_name=_('Fecha de Salida del país'), null=True)
    # letter = TextField(verbose_name=_('Carta Migratoria'), null=True)
    # invitation_file = BooleanField(verbose_name=_('¿Email de Invitación?'), default=False)
    # diploma = BooleanField(verbose_name=_('¿Email de Diploma?'), default=False)
    #
