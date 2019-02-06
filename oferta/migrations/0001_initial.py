# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-05 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('requirements', models.CharField(max_length=1000)),
                ('experience', models.CharField(choices=[(b'0', b'Experi\xc3\xa8ncia no requerida'), (b'1', b'Al menys un any'), (b'2', b'Al menys dos any'), (b'3', b'M\xc3\xa9s de 3 anys')], max_length=1, null=True)),
                ('minimum_requirements', models.CharField(max_length=5000)),
                ('description', models.CharField(max_length=40000, null=True)),
                ('numero_de_vacants', models.IntegerField(null=True)),
                ('salari', models.CharField(max_length=200, null=True)),
                ('nomempresadelaoferta', models.CharField(blank=True, max_length=1000, null=True)),
                ('empresadelaoferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ofertainscrits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oferta.Oferta')),
            ],
        ),
        migrations.AddField(
            model_name='oferta',
            name='oferta_inscrits',
            field=models.ManyToManyField(through='oferta.ofertainscrits', to='student.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='ofertainscrits',
            unique_together=set([('estudiant', 'oferta')]),
        ),
    ]
