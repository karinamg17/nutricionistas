# Generated by Django 3.1.13 on 2021-12-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutri_app', '0005_datosbiomedicos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cita',
            options={'ordering': ('-fecha',)},
        ),
        migrations.AddField(
            model_name='datosbiomedicos',
            name='comidas',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='datosbiomedicos',
            name='estilo_de_vida',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='datosbiomedicos',
            name='habitos',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='datosbiomedicos',
            name='preferencias_alimentarias',
            field=models.JSONField(default=dict),
        ),
    ]
