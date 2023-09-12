# Generated by Django 4.2.5 on 2023-09-12 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Primer nombre')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Segundo nombre')),
                ('surname', models.CharField(max_length=50, verbose_name='Primer apellido')),
                ('lastname', models.CharField(max_length=50, verbose_name='Segundo apellido')),
                ('birth', models.DateField(verbose_name='Fecha de nacimiento')),
                ('country', models.CharField(max_length=50, verbose_name='País de naciemiento')),
                ('gender', models.CharField(max_length=50, verbose_name='Genero')),
                ('status', models.CharField(max_length=50, verbose_name='Estado civíl')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
