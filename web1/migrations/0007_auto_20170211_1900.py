# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0006_auto_20170301_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrocinadores',
            name='logo',
            field=models.ImageField(upload_to='paginas/patrocinadores/', verbose_name='logo'),
        ),
    ]