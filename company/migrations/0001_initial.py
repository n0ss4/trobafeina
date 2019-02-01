# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-01 15:20
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
            name='Company',
            fields=[
                ('cif', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name=b'CIF')),
                ('sector', models.CharField(max_length=500)),
                ('descripcio', models.TextField(max_length=500, verbose_name=b'Descripci\xc3\xb3')),
                ('nomResponsable', models.CharField(max_length=500, verbose_name=b'Nom del responsable')),
                ('cognomResponsable', models.CharField(max_length=500, verbose_name=b'Cognom del responsable')),
                ('esempresaa', models.BooleanField(default=True)),
                ('nomusuari', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Nom del usuari')),
            ],
        ),
    ]
