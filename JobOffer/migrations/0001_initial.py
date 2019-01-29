# Generated by Django 2.1.5 on 2019-01-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joboffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('requirements', models.CharField(max_length=1000)),
                ('experience', models.CharField(choices=[('no', 'Experiència no requerida'), ('1', 'Al menys un any'), ('2', 'Al menys dos any'), ('3', 'Més de 3 anys')], max_length=1, null=True)),
                ('minimum_requirements', models.CharField(max_length=5000)),
                ('description', models.CharField(blank=True, max_length=40000)),
                ('numero_de_vacants', models.IntegerField(null=True)),
                ('salari', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]