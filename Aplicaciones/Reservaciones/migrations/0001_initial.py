# Generated by Django 5.1.3 on 2025-01-10 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('tipo_de_alojamiento', models.CharField(max_length=100)),
                ('número_de_personas', models.CharField(max_length=100)),
                ('estado_de_la_reserva', models.CharField(max_length=100)),
                ('observacion', models.TextField()),
                ('campista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservaciones.campista')),
            ],
        ),
    ]
