from django.db import models
from datetime import datetime

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
  
# Modelo que representa la reserva de un servicio      
class ReservaServicio(models.Model):
    fecha_creacion = models.DateTimeField(default= datetime.now())
    fecha_reserva = models.DateTimeField(default= datetime.today())
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    #responsable = models.ForeignKey(Coordinador, null=False, blank=False, on_delete=models.CASCADE)
    #empleado = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
    #servicio = models.ForeignKey(Servicio, null=False, blank=False, on_delete=models.CASCADE)
    precio = models.PositiveBigIntegerField(null=False, blank=False)
    
    # Método que devuelve una representación legigle de ReservaDeServicio en forma de cadena
    def __str__(self):
        return f'Reserva De Servicio: {self.fecha_creacion}, {self.cliente}, {self.precio}, {self.fecha_reserva}'
    
    # Clase que proporciona información útil sobre cómo se almacenan y representan los datos 
    # de una reserva de servicio, así como cómo se ordenan las instancias de la reserva por defecto en consultas de base de datos.
    class Meta:
        ordering = ['fecha_creacion', 'cliente', 'precio']