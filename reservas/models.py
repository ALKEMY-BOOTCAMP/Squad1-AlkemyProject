from django.db import models
from datetime import datetime


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    # Método que devuelve una representación legigle de Cliente en forma de cadena
    def __str__(self):
        return f' Cliente: {self.apellido.upper()}, {self.nombre.lower()}, Activo: {self.activo}'

    # Clase que proporciona información útil sobre cómo se almacenan y representan los datos
    # de un cliente, así como cómo se ordenan las instancias de cliente por defecto en consultas de base de datos.

    class Meta:
        ordering = ['activo', 'apellido', 'nombre']


class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Servicio: {self.nombre.upper()}, Precio: ${self.precio} | [ {self.activo} ] "


class Meta:
    ordering = ['nombre', 'precio', 'activo']


# Modelo Empleado
class Empleado(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    numero_de_legajo = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Modelo que representa la reserva de un servicio
class ReservaServicio(models.Model):
    fecha_creacion = models.DateTimeField(default=datetime.now())
    fecha_reserva = models.DateTimeField(default=datetime.today())
    cliente = models.ForeignKey(
        Cliente, null=False, blank=False, on_delete=models.CASCADE)
    # responsable = models.ForeignKey(Coordinador, null=False, blank=False, on_delete=models.CASCADE)
    # empleado = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
    # servicio = models.ForeignKey(Servicio, null=False, blank=False, on_delete=models.CASCADE)
    precio = models.PositiveBigIntegerField(null=False, blank=False)

    # Método que devuelve una representación legigle de ReservaDeServicio en forma de cadena
    def __str__(self):
        return f'Reserva De Servicio: {self.fecha_creacion}, {self.cliente}, {self.precio}, {self.fecha_reserva}'

    # Clase que proporciona información útil sobre cómo se almacenan y representan los datos
    # de una reserva de servicio, así como cómo se ordenan las instancias de la reserva por defecto en consultas de base de datos.
    class Meta:
        ordering = ['fecha_creacion', 'cliente', 'precio']


class Coordinador(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido = models.CharField(max_length=30, null=False, blank=False)
    numero_documento = models.IntegerField(blank=False, null=False)
    fecha_alta = models.DateTimeField(default=datetime.today())
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Coordinador: {self.activo}, {self.apellido}, {self.nombre}, {self.numero_documento}, {self.fecha_alta}'

    class Meta:
        ordering = ['activo', 'apellido', 'numero_documento']
