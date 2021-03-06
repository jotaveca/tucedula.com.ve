# Generated by Django 3.0.6 on 2020-05-15 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCedulaBetaApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cedula',
            old_name='cedula',
            new_name='nu_cedula',
        ),
        migrations.RenameField(
            model_name='cedula',
            old_name='direccion',
            new_name='tx_direccion',
        ),
        migrations.RemoveField(
            model_name='cedula',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='cedula',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='cedula',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='cedula',
            name='parroquia',
        ),
        migrations.AddField(
            model_name='cedula',
            name='tx_centro_electoral',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cedula',
            name='tx_estado',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cedula',
            name='tx_municipio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cedula',
            name='tx_nac',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cedula',
            name='tx_nombre_apellido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cedula',
            name='tx_parroquia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
