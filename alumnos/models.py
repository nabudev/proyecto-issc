from django.db import models

# Create your models here.

class Carreras(models.Model):
    IDcarrera= models.IntegerField(primary_key=True)
    nombre= models.TextField()
    duracion=models.IntegerField()
    horario= models.CharField(max_length=20)
    
class Alumnos(models.Model):
    DNI= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=25)
    apellido= models.CharField(max_length=25)
    edad= models.IntegerField()
    carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    
class Materias(models.Model):
    IDmateria=models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=40)
    duracion= models.CharField(max_length=50)
    horario=models.CharField(max_length=20)
    carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)

    