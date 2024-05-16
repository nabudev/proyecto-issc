from django.db import models

# Create your models here.

class Carreras(models.Model):
    id_carrera= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=40)
    duracion=models.CharField(max_length=10)
    horario= models.CharField(max_length=20)
    precio=models.IntegerField()
    
    def __str__(self):
        return self.nombre

    
class Alumnos(models.Model):
    dni= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=25)
    apellido= models.CharField(max_length=25)
    direccion= models.CharField(max_length=30)
    contacto=models.CharField(max_length=40)
    id_carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.dni}'
    
class Materias(models.Model):
    id_materia=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=40)
    duracion= models.CharField(max_length=50)
    horario=models.CharField(max_length=20)
    id_carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Matricula(models.Model):
    id_matricula= models.AutoField(primary_key=True)
    precio_matricula= models.CharField(max_length=11)
    precio_seguro=models.CharField(max_length=10)
    dni= models.ForeignKey(Alumnos,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.dni.dni)

class Metodo_pago(models.Model):
    tipo= models.CharField(max_length=15)
    
    def __str__(self):
        return self.tipo

class Meses(models.Model):
    mes= models.CharField(max_length=20)
    
    def __str__(self):
        return self.mes
    
class Pagos(models.Model):
    id_pagos=models.AutoField(primary_key=True)
    dni= models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    id_carrera= models.ForeignKey(Carreras, on_delete=models.CASCADE)
    monto= models.CharField(max_length=10)
    fecha= models.DateField()
    observacion= models.CharField(max_length=50)
    metodo_de_pago=models.ForeignKey(Metodo_pago, on_delete=models.CASCADE)
    mes= models.ForeignKey(Meses, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.dni.dni) + ' ' + str(self.fecha)
    

    

    

    