# Generated by Django 4.2.5 on 2023-09-12 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_persona_document_number_persona_document_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], max_length=1, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='status',
            field=models.CharField(choices=[('1', 'Soltero'), ('2', 'Casado'), ('3', 'Unión libre'), ('4', 'Separado'), ('4', 'Divorciado'), ('4', 'Viudo')], max_length=1, verbose_name='Estado civíl'),
        ),
    ]