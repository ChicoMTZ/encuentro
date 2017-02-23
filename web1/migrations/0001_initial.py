# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 10:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='centro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(blank=True, verbose_name='Fecha inicio')),
                ('date_end', models.DateField(blank=True, verbose_name='Fecha Final')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Titulo')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Pais')),
                ('places', models.CharField(blank=True, max_length=100, verbose_name='Lugar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='enlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_social', models.CharField(choices=[(b'Facebook', b'Facebook'), (b'Twitter', b'Twitter')], max_length=8, verbose_name='Red social')),
                ('direccion', models.URLField(verbose_name='Direccion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='pagina_web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to=b'paginas/logos/', verbose_name='logo')),
                ('banner', models.ImageField(upload_to=b'paginas/banner/', verbose_name='banner')),
                ('slogan', models.CharField(max_length=100, verbose_name='Slogan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('web', models.URLField(verbose_name='Web')),
                ('logo', models.ImageField(upload_to=b'logos/', verbose_name='logo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_url', models.CharField(max_length=255, verbose_name='Nombre Evento')),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
