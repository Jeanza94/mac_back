from django.db import models

class Persona(models.Model):
    firstname = models.CharField('Primer nombre', max_length=50)
    middle_name = models.CharField('Segundo nombre', max_length=50)
    surname = models.CharField('Primer apellido', max_length=50)
    lastname = models.CharField('Segundo apellido', max_length=50)
    birth = models.DateField('Fecha de nacimiento')
    country = models.CharField('País de nacimiento', max_length=50)
    gender = models.CharField('Genero', max_length=50)
    status = models.CharField('Estado civíl', max_length=50)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return f'{self.id} - {self.firstname} - {self.surname}'
    
    
    
