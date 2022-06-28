from django.contrib import admin
from .models import Cursos

# Register your models here.

class cursomod(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Cursos, cursomod)
