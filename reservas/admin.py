from django.contrib import admin
from .models import Servicio, Empleado, Coordinador

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')
    search_fields = ('nombre',) #Busqueda por nombre
    list_filter = ('activo',)



class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_de_legajo', 'activo')
    search_fields = ('nombre', 'apellido') #Busqueda por nombre
    list_filter = ('activo',)
    
class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero_documento','fecha_alta', 'activo')
    search_fields = ('nombre', 'apellido') #Busqueda por nombre
    list_filter = ('activo',)

admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Coordinador, CoordinadorAdmin)
