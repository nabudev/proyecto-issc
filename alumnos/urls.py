from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('pagos/<int:dni>/', views.pagos)
]