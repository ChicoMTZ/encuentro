# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-10 02:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji_alt', models.CharField(max_length=50, verbose_name='Emoji')),
                ('nombre', models.CharField(max_length=100, verbose_name='Categor\xeda')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField(verbose_name='Respuestas')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creaci\xf3n')),
                ('publicada', models.BooleanField(verbose_name='Publicado')),
                ('pregunta', models.TextField(verbose_name='Pregunta')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faq.CategoriaPregunta', verbose_name='Categoria')),
            ],
        ),
    ]
