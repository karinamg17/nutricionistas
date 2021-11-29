# Generated by Django 3.1.13 on 2021-11-19 11:18

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='accept_terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de nacimiento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='foto_usuario',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Suba un foto en formato jpge o png', null=True, upload_to='images/foto_perfil', verbose_name='Foto perfil de usuario'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='nro_documento',
            field=models.CharField(default='', max_length=12, unique=True, verbose_name='Nro. de documento'),
        ),
        migrations.AddField(
            model_name='user',
            name='nro_telefono',
            field=models.CharField(default='', max_length=12, unique=True, verbose_name='Nro. de teléfono'),
        ),
        migrations.AddField(
            model_name='user',
            name='tipo_documento',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='Cédula', max_length=100, no_check_for_status=True),
        ),
    ]
