from django.urls import path
from . import views

urlpatterns = [
    path('software/', views.software),
    path('rrhh/', views.rrhh)
]