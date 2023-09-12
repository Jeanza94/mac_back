from django.db import models
from .managers import PersonaManger

class Persona(models.Model):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    
    DOCUMENT_TYPES_CHOICES = (
        ('1', 'Cedula'),
        ('2', 'Pasaporte'),
        ('3', 'Visa'),
        ('4', 'Otro'),
    )

    STATUS_CHOICES = (
        ('1', 'Soltero'),
        ('2', 'Casado'),
        ('3', 'Unión libre'),
        ('5', 'Separado'),
        ('6', 'Divorciado'),
        ('7', 'Viudo'),
    )

    firstname = models.CharField('Primer nombre', max_length=50)
    middle_name = models.CharField('Segundo nombre', max_length=50)
    surname = models.CharField('Primer apellido', max_length=50)
    lastname = models.CharField('Segundo apellido', max_length=50)
    birth = models.DateField('Fecha de nacimiento')
    country = models.CharField('País de nacimiento', max_length=50)
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    status = models.CharField('Estado civíl', max_length=1, choices= STATUS_CHOICES)
    document_type= models.CharField('Tipo de documento', max_length=1, choices=DOCUMENT_TYPES_CHOICES, null=True)
    document_number = models.IntegerField('Número del documento', null=True, unique=True)

    objects = PersonaManger()

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return f'{self.id} - {self.document_number} - {self.firstname} - {self.surname}'
    
    
    
