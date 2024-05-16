from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pagos, Alumnos
# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a la gestion alumnos</h1>')

def pagos(request, dni):
    alumno= get_object_or_404(Alumnos, dni=dni)
    pagos = Pagos.objects.filter(dni=alumno)
    context = {'alumno': alumno,'pagos': pagos}
    return render(request, 'pagos.html', context)