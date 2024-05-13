from django.db import models

# Create your models here.

class Carreras(models.Model):
    id_carrera= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=40)
    duracion=models.CharField(max_length=10)
    horario= models.CharField(max_length=20)
    precio=models.IntegerField()
    
class Alumnos(models.Model):
    dni= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=25)
    apellido= models.CharField(max_length=25)
    edad= models.CharField(max_length=2)
    id_carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    
class Materias(models.Model):
    id_materia=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=40)
    duracion= models.CharField(max_length=50)
    horario=models.CharField(max_length=20)
    id_carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    
class Matricula(models.Model):
    id_matricula= models.AutoField(primary_key=True)
    precio_matricula= models.CharField(max_length=11)
    precio_seguro=models.CharField(max_length=10)
    dni= models.ForeignKey(Alumnos,on_delete=models.CASCADE)
    
class Pagos(models.Model):
    id_pagos=models.AutoField(primary_key=True)
    dni= models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    id_carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    monto= models.CharField(max_length=10)
    fecha= models.DateField()
    observacion= models.CharField(max_length=50)
    
class Metodo_pago(models.Model):
    tipo= models.CharField(max_length=15)
    