from django.contrib import admin
from .models import Empleado

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero de legajo', 'activo')
    search_fields = ('nombre', 'apellido') #Busqueda por nombre
    list_filter = ('activo',)

admin.site.register(Empleado)
