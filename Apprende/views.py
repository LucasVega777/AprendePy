from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from .models import Autor
# Create your views here.

def inicio(request):
    return render(request, "inicio.html")


def cursos(request):
    lista_cursos = Curso.objects.order_by("nombreCurso")
    nombre_cursos = { "name": lista_cursos, "titulo": "Cursos" }
    return render(request, "cursos.html", nombre_cursos)


def contacto(request):
    return render(request, "contacto.html")


def about(request):
    return render(request, "about.html")


def faq(request):
    return render(request, "faq.html")


def autores(request):
    lista_autores = Autor.objects.order_by("nombreAutor")
    nombre_Autores = { "name": lista_autores, "titulo": "Autores" }
    return render(request, "autores.html", nombre_Autores)


def fautores(request, nombre):
    resultado = Autor.objects.filter(nombreAutor__icontains=nombre)
    if (len(resultado)==1):
        titulo = "Autor"
    elif(len(resultado)>1):
        titulo = "Autores"
    else:
        titulo = "No se encontraron Resultados"
    nombre_Autores = {'name':resultado, "titulo": titulo}
    return render(request, 'autores.html', nombre_Autores)


def fcursos(request,nombre):
    resultado = Curso.objects.filter(nombreCurso__icontains=nombre)
    if (len(resultado)==1):
        titulo = "Curso"
    elif(len(resultado)>1):
        titulo = "Cursos"
    else:
        titulo = "No se encontraron Resultados"
    nombre_Cursos = {'name': resultado, "titulo": titulo}
    return render(request, "cursos.html", nombre_Cursos)