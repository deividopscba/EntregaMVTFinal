from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechadenacimiento = models.DateField()
    id = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    email = models.EmailField()

class Medico(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechadenacimiento = models.DateField()
    id = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)