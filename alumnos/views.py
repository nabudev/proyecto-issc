from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pagos, Alumnos
# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a la gestion alumnos</h1>')

def pagos(request):
    pagos=list(Pagos.objects.values())
    return JsonResponse(pagos, safe=False)

def alumnos(request):
    alumnos= list(Alumnos.objects.values())
    return JsonResponse(alumnos, safe=False)