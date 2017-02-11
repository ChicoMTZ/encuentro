# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-01 07:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
        ('web1', '0005_auto_20170301_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='enlaces',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patrocinadores',
            name='sites',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Sitios'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webbuilder',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enlaces',
            name='sites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Sitios'),
        ),
        migrations.AlterField(
            model_name='webbuilder',
            name='sites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Sitios'),
        ),
    ]