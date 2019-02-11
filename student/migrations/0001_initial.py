# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-11 14:53
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
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=b'', max_length=100, verbose_name=b'Nom')),
                ('cognom', models.CharField(default=b'', max_length=100, verbose_name=b'Cognom')),
                ('dni', models.CharField(default=b'', max_length=100, unique=True, verbose_name=b'DNI')),
                ('adreca', models.CharField(default=b'', max_length=100, verbose_name=b'Adre\xc3\xa7a')),
                ('poblacio', models.CharField(default=b'', max_length=100, verbose_name=b'Poblaci\xc3\xb3')),
                ('codi_postal', models.CharField(default=b'', max_length=100, verbose_name=b'Codi Postal')),
                ('telefon', models.CharField(default=b'', max_length=100, verbose_name=b'Tel\xc3\xa8fon')),
                ('correu_electronic', models.CharField(default=b'', max_length=100, verbose_name=b'Correu electronic')),
                ('edat', models.CharField(default=b'', max_length=100, verbose_name=b'Edat')),
                ('estudis', models.CharField(default=b'', max_length=1000, verbose_name=b'Estudis')),
                ('experiencia', models.CharField(default=b'', max_length=1000, verbose_name=b'Experiencia')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Nom del usuari')),
            ],
        ),
    ]
