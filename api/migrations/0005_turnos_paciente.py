# Generated by Django 5.1.2 on 2024-10-17 21:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_turnos_paciente_paciente_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.paciente'),
        ),
    ]
