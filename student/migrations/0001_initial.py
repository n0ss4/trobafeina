# Generated by Django 2.1.5 on 2019-01-30 14:09

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
                ('experiencia', models.CharField(default='', max_length=40000)),
                ('estudis', models.CharField(blank=True, default='', max_length=400)),
                ('idiomes', models.CharField(blank=True, default='', max_length=400)),
                ('coneixements', models.CharField(blank=True, default='', max_length=400)),
                ('carnet_de_conduir', models.CharField(blank=True, default='', max_length=400)),
                ('situacio_laboral', models.CharField(blank=True, default='', max_length=400)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nom del usuari')),
            ],
        ),
    ]
