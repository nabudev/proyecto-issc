from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pagos
# Create your views here.

def pagos(request):
    pagos=list(Pagos.objects.values())
    return JsonResponse(pagos, safe=False)