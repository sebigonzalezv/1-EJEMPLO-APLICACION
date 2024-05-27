from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

def curso(req, nombre, camada):
    nuevo_curso = Curso(nombre=nombre, camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"Curso: {nuevo_curso.nombre} - Camada: {nuevo_curso.camada} creado!")

def lista_cursos(req):
    lista = Curso.objects.all()
    return render(req, "lista_cursos.html", {"lista_cursos": lista})

# Create your views here.