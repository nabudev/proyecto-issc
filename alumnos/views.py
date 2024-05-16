from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pagos, Alumnos
# Create your views here.

def index(request):
    return render(request, 'index.html')

def alumnos(request):
    return render(request, 'alumnos.html')

def pagos(request, dni):
    alumno= get_object_or_404(Alumnos, dni=dni)
    pagos = Pagos.objects.filter(dni=alumno)
    context = {'alumno': alumno,'pagos': pagos}
    return render(request, 'pagos.html', context)