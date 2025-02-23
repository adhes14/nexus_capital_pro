# Generated by Django 5.0.7 on 2024-07-20 02:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mercado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, unique=True)),
                ('horario', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, unique=True)),
                ('ticker', models.CharField(max_length=40, unique=True)),
                ('mercado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activo.mercado')),
            ],
        ),
        migrations.CreateModel(
            name='PrecioHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('precio_cierre', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moneda', models.CharField(choices=[('usd', 'DOLAR'), ('eur', 'EURO')], default='usd', max_length=3)),
                ('activo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activo.activo')),
            ],
        ),
    ]
