"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from cursos import views as vCursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vCursos.cursos, name="principal"),
    #path('', views.principal, name="principal"),
    path('formulario/',views.form, name="formulario"),
    #path('contacto/',views.contact, name="contacto"),
    path('registrar/',vCursos.registrar, name="registrar"),
    path('contacto/',vCursos.contacto,name='contacto'),
    #path('ejemplo/',views.ejemplo,name='ejemplo'),
    path('comentario/',vCursos.registrar, name="comentario"),
    path('eliminarComentario/<int:id>/',vCursos.eliminarComentarioContacto, name='Eliminar'),
    path('formEditarComentario/<int:id>/', vCursos.consultarComentario, name='ConsultarIndividual'),
    path('editarComentario/<int:id>/', vCursos.editarComentario, name='Editar'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

