from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pagos, Alumnos
# Create your views here.


def pagos(request):
    pagos=list(Pagos.objects.values())
    return JsonResponse(pagos, safe=False)

def alumnos(request):
    alumnos= list(Alumnos.objects.values())
    return JsonResponse(alumnos, safe=False)