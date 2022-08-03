from django.shortcuts import render
from .models import Cursos, Comentario, ComCont
from .forms import ComContForm
from django.shortcuts import get_object_or_404

def cursos(request):
    cursos=Cursos.objects.all()
    return render(request,"cursos/principal.html",{'cursos':cursos})

def registrar(request):
    if request.method == 'POST':
        form = ComContForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios=ComCont.objects.all()
            return render(request,'cursos/comentarios.html', {'comentarios': comentarios})
    form = ComContForm()
    return render(request,'cursos/contacto.html',{'form': form})

def eliminarComentarioContacto(request, id,
    confirmacion='cursos/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComCont, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComCont.objects.all()
        return render(request,'cursos/comentarios.html', {'comentarios': comentarios})
    return  render(request, confirmacion, {'object':comentario})

def consultarComentario(request, id):
    comentario = ComCont.objects.get(id=id)
    return render(request, 'cursos/formeditcomentario.html', {'comentario': comentario})

def editarComentario(request, id):
    comentario = get_object_or_404(ComCont, id=id)
    form = ComContForm(request.POST, instance=comentario)
    
    if form.is_valid():
        form.save()
        comentarios = ComCont.objects.all()
        return render(request, 'cursos/comentarios.html', {'comentarios': comentarios})
    return render(request, 'cursos/formeditcomentario.html', {'comentario':comentario })

def contacto(request):
    return render(request,"cursos/contacto.html")

def coment(request):
    comentarios = ComCont.objects.all()
    return render(request, 'cursos/comentarios.html', {'comentarios': comentarios})