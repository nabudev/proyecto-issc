from django.urls import path
from . import views

urlpatterns = [
    path('pagos/', views.pagos),
    path('alumnos/', views.alumnos)
]