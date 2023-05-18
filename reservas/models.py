from django.db import models


# Create your models here.

class Servicio(models.Model):  
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null = True)
    precio = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Servicio: {self.nombre.upper()}, Precio: ${self.precio} | [ {self.activo} ] "

class Meta:
    ordering = ['nombre','precio','activo']
    
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    # Otros campos que necesites para el modelo Empleado
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"