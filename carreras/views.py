from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def software(request):
    return HttpResponse('<h1>Tecnicatura Superior en Desarrollo de Software</h1>')

def rrhh(request):
    return HttpResponse('<h1>Tecnicatura Superior en Gestión de los Recursos Humanos</h1>')