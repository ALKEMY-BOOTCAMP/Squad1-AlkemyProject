from django.contrib import admin
from .models import Cliente

# Register your models here.

# Definición de la clase ClienteAdmin que hereda de admin.ModelAdmin
class ClienteAdmin(admin.ModelAdmin):
    # list_display: Campos a mostrar en la lista de objetos del modelo
    list_display = ('nombre', 'apellido', 'activo')

    # list_search: Campos por los que se puede buscar en la lista de objetos del modelo
    list_search = ('apellido',)

    # list_filter: Campos por los que se pueden filtrar los objetos en la lista
    list_filter = ('activo',)

# Registrar el modelo Cliente junto con la configuración del administrador en el panel de administración
admin.site.register(Cliente, ClienteAdmin)

# Definición de la clase ReservaServicioAdmin que gereda de admin.ModelAdmin
class ReservaServicioAdmin(admin.ModelAdmin):
    #list_display: Campos para mostrar en la lista de objetos del modelo
    list_display = ('fecha_creacion','fecha_reserva','cliente','precio')
    
    #list_search: Campos los que se puede buscar en la lista de objetos del modelo
    list_search = ('fecha_creacion','fecha_reserva')
    
    # list_filter: Campos por los que se puede filtrar objetos en la lista
    #list_filter = ('coordinador', 'cliente', 'empleado','servicio')