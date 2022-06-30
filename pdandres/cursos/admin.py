from msilib import sequence
from django.contrib import admin
from .models import Cursos

# Register your models here.

class cursomod(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombrecurso','turno')
    search_fields = ('nombrecurso','nombreprof')
    date_hierarchy = 'created'
    list_filter = ('evaluacion','turno')

admin.site.register(Cursos, cursomod)
