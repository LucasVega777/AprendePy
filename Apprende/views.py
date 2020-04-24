from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

def inicio(request):
    return render(request, "inicio.html")


def cursos(request):
    lista_cursos = Curso.objects.order_by("nombreCurso")
    nombre_cursos = { "name": lista_cursos }
    return render(request, "cursos.html", nombre_cursos)


def contacto(request):
    return render(request, "contacto.html")


def about(request):
    return render(request, "about.html")


def faq(request):
    return render(request, "faq.html")


