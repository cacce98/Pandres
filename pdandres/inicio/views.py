from django.http import HttpResponse
from django.shortcuts import render, HttpResponse



# Create your views here.

def principal(request):
    
    return render(request, "inicio/principal.html")

def form(request):

    return render(request, "inicio/formulario.html")

def contact(request):

    return render(request, "inicio/contact.html")