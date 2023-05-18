from django.db import models

# Create your models here.
class Empleado(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    numero_de_legajo = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
      

