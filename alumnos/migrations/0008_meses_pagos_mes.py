# Generated by Django 5.0.6 on 2024-05-16 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0007_remove_alumnos_edad_alumnos_contacto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='pagos',
            name='mes',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='alumnos.meses'),
            preserve_default=False,
        ),
    ]