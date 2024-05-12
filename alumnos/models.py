from django.db import models

# Create your models here.

class Carreras(models.Model):
    ID_carrera= models.AutoField(primary_key=True)
    nombre= models.TextField()
    duracion=models.IntegerField()
    horario= models.CharField(max_length=20)
    precio=models.CharField(max_length=10)
    
class Alumnos(models.Model):
    DNI= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=25)
    apellido= models.CharField(max_length=25)
    edad= models.IntegerField()
    ID_carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    
class Materias(models.Model):
    ID_materia=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=40)
    duracion= models.CharField(max_length=50)
    horario=models.CharField(max_length=20)
    ID_carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    
class Matricula(models.Model):
    ID_matricula= models.AutoField(primary_key=True)
    precio_matricula= models.IntegerField()
    precio_seguro=models.IntegerField()
    DNI= models.ForeignKey(Alumnos,on_delete=models.CASCADE)
    
class Pagos(models.Model):
    ID_pagos=models.AutoField(primary_key=True)
    DNI= models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    ID_carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    monto= models.CharField(max_length=10)
    fecha= models.DateField()
    observacion= models.CharField(max_length=50)
    

    