# Generated by Django 5.1.3 on 2025-01-10 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reservaciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recomendacion',
            new_name='Reservacion',
        ),
        migrations.RenameField(
            model_name='reservacion',
            old_name='número_de_personas',
            new_name='numero_de_personas',
        ),
    ]
