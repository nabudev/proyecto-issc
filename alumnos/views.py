from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pagos, Alumnos
# Create your views here.

def index(request):
    return render(request, 'index.html')

def pagos(request):
    pagos = Pagos.objects.all()
    context = {'pagos': pagos}
    return render(request, 'pagos.html', context)

def alumnos(request):
    alumnos= list(Alumnos.objects.values())
    context= {'alumnos': alumnos}
    return render(request, 'alumnos.html', context)