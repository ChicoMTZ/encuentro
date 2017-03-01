# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from web1.models import Eventos
from django.contrib.sites.models import Site


class TshirtStyle(Model):
    gender_choice = (
        ('M', 'Masculino'),
        ('F', 'Femenino')

    )

    description = TextField(verbose_name=_('Descripción'))
    gender = CharField(max_length=1, choices=gender_choice, verbose_name=_('Género'))
    img1 = ImageField(verbose_name=_('Imagen 1'), upload_to='Tshirt/')
    img2 = ImageField(verbose_name=_('Imagen 2'), upload_to='Tshirt/')
    img3 = ImageField(verbose_name=_('Imagen 3'), upload_to='Tshirt/')

    name = CharField(max_length=45, verbose_name=_('Nombre'))
    price = DecimalField(verbose_name=_('Precio'), decimal_places=2, max_digits=6)
    sites = ForeignKey(Site, on_delete=CASCADE, verbose_name=_('Sitios'))

    def __str__(self):
        return self.name


class Tshirt(Model):
    style = ForeignKey(TshirtStyle, on_delete=CASCADE, verbose_name=_('Estilo'))
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('Usuario'))
    amount = PositiveIntegerField(verbose_name=_('Cantidad'))
    last_update = DateField(verbose_name=_('Última Actualización'))
    size = CharField(max_length=15, verbose_name=_('Talla'))
    pagada = BooleanField(default=False)

    def __str__(self):
        return self.style.name + ' ' + self.style.description

