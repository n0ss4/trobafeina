# Generated by Django 2.1.5 on 2019-01-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20190126_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='carnet_de_conduir',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='student',
            name='coneixements',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='student',
            name='estudis',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='student',
            name='experiencia',
            field=models.CharField(default='', max_length=40000),
        ),
        migrations.AddField(
            model_name='student',
            name='idiomes',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='student',
            name='situacio_laboral',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]