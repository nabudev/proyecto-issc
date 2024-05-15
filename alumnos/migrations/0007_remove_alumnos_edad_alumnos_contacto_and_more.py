# Generated by Django 5.0.6 on 2024-05-14 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0006_pagos_metodo_de_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='edad',
        ),
        migrations.AddField(
            model_name='alumnos',
            name='contacto',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='direccion',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]