from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombrecurso = models.CharField(max_length=12,verbose_name="Nombre del curso")
    nombreprof = models.TextField(verbose_name="Nombre del profesor")
    duracion = models.TextField(verbose_name="Duracion del curso")
    evaluacion = models.TextField(verbose_name="Tipo de evaluacion")
    turno = models.CharField(max_length=10,verbose_name="Turno en el que se imparte")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = "Curso"
    verbose_name_plural = "Cursos"
    ordering = ["-creado"]

def __str__(self):  # return number position model
        return self.nombrecurso