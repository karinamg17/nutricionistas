# Generated by Django 3.1.13 on 2021-11-28 12:45

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
            name='PeriodoMenstrual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_menstruacion', models.CharField(blank=True, max_length=2, null=True)),
                ('fecha_ultima_menstruacion', models.DateField(blank=True, null=True)),
                ('sintomas_antes', models.CharField(blank=True, max_length=100, null=True)),
                ('sintomas_despues', models.CharField(blank=True, max_length=100, null=True)),
                ('embarazo', models.BooleanField(default=False)),
                ('anticonceptivos', models.BooleanField(default=False)),
                ('anticonceptivos_cuales', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nutri_paciente_periodo_mestrual', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndicadorBioquimico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('colesterol', models.CharField(blank=True, max_length=10, null=True)),
                ('trigliceridos', models.CharField(blank=True, max_length=10, null=True)),
                ('hdl', models.CharField(blank=True, max_length=10, null=True)),
                ('ldl', models.CharField(blank=True, max_length=10, null=True)),
                ('glucosa_ayunas', models.CharField(blank=True, max_length=10, null=True)),
                ('hemoglobina', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutri_paciente_indicadores_bioquimicos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('diaganotico', models.TextField()),
                ('completada', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutri_paciente_cita', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
