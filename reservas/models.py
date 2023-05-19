from django.db import models

# Create your models here.
# Modelo que representa un cliente en el sistema
class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    
    # Método que devuelve una representación legigle de Cliente en forma de cadena
    def __str__(self):
        return f' Cliente: {self.apellido.upper()}, {self.nombre.lower()}, Activo: {self.activo}'
    
    
    # Clase que proporciona información útil sobre cómo se almacenan y representan los datos 
    # de un cliente, así como cómo se ordenan las instancias de cliente por defecto en consultas de base de datos.
    class Meta:
        ordering = ['activo', 'apellido','nombre']