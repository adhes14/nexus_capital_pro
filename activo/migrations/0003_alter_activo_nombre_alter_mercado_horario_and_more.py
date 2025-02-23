# Generated by Django 5.0.7 on 2024-07-20 20:01

import activo.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activo', '0002_alter_mercado_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo',
            name='nombre',
            field=models.CharField(max_length=80, unique=True, validators=[activo.validators.validar_no_caracteres_especiales]),
        ),
        migrations.AlterField(
            model_name='mercado',
            name='horario',
            field=models.TimeField(blank=True, null=True, validators=[activo.validators.validar_hora]),
        ),
        migrations.AlterField(
            model_name='mercado',
            name='nombre',
            field=models.CharField(max_length=80, unique=True, validators=[activo.validators.validar_no_caracteres_especiales]),
        ),
    ]
