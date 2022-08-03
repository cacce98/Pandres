from re import T
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from xml.etree.cElementTree import Comment
from django.db import models
from ckeditor.fields import RichTextField

class Cursos(models.Model):
    nombrecurso = models.CharField(max_length=12,verbose_name="Nombre del curso")
    nombreprof = models.TextField(verbose_name="Nombre del profesor")
    duracion = models.TextField(verbose_name="Duracion del curso")
    evaluacion = models.TextField(verbose_name="Tipo de evaluacion")
    turno = models.CharField(max_length=10,verbose_name="Turno en el que se imparte")
    fotos = models.ImageField(null=True, upload_to="imagenes",verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):  # return number position model
        return self.nombrecurso
class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE,verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment = models.TextField(verbose_name="Comentario")
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["created"]

    def __str__(self):
        return self.coment

class ComCont(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    
    class Meta:
        verbose_name = "Comentario de Contacto"
        verbose_name = "Comentarios de Contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje