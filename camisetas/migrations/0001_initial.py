# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-10 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tshirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('last_update', models.DateField(verbose_name='\xdaltima Actualizaci\xf3n')),
                ('size', models.CharField(max_length=15, verbose_name='Talla')),
                ('pagada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TshirtStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descripci\xf3n')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='G\xe9nero')),
                ('img1', models.ImageField(upload_to='Tshirt/', verbose_name='Imagen 1')),
                ('img2', models.ImageField(upload_to='Tshirt/', verbose_name='Imagen 2')),
                ('img3', models.ImageField(upload_to='Tshirt/', verbose_name='Imagen 3')),
                ('name', models.CharField(max_length=45, verbose_name='Nombre')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio')),
            ],
        ),
    ]
