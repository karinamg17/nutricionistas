# Generated by Django 3.1.13 on 2021-12-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutri_app', '0011_datosbiomedicos_actividad_fisica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deporte',
            name='duraciion',
        ),
        migrations.AddField(
            model_name='deporte',
            name='duracion',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
