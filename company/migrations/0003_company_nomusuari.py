# Generated by Django 2.1.5 on 2019-01-31 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_company_esempresaa11'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='nomusuari',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
