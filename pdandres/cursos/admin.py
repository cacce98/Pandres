from msilib import sequence
from django.contrib import admin
from .models import Cursos, ComCont
from .models import Comentario

# Register your models here.

class cursomod(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombrecurso','turno')
    search_fields = ('nombrecurso','nombreprof')
    date_hierarchy = 'created'
    list_filter = ('evaluacion','turno')

admin.site.register(Cursos, cursomod)

class AdComentarios(admin.ModelAdmin):
    readonly_fields = ('created','id')
    list_display = ('id', 'coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'

admin.site.register(Comentario, AdComentarios)
class AdComconts(admin.ModelAdmin):
    readonly_fields = ('created','id')
    ist_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'

admin.site.register(ComCont, AdComconts)
