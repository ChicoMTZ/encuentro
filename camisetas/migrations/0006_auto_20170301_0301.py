# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-01 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camisetas', '0005_remove_tshirtstyle_eventos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirtstyle',
            name='sites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Sitios'),
        ),
    ]