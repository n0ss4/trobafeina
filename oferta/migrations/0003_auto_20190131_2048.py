# Generated by Django 2.1.5 on 2019-01-31 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oferta', '0002_auto_20190131_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='empresadelaoferta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
        ),
    ]
