from datetime import date
from django.db import models
from apps.persona.models import Persona

# Create your models here.
class Tarea(models.Model):
    title = models.CharField('Titulo', max_length=100, unique=True)
    description = models.TextField('Descripción', max_length=100)
    person = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tasks')
    limit_date = models.DateField('Fecha limite', default=date.today)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return f'{self.id} - {self.title}'