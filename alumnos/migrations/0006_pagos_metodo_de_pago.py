# Generated by Django 5.0.6 on 2024-05-13 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_metodo_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='metodo_de_pago',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='alumnos.metodo_pago'),
            preserve_default=False,
        ),
    ]
