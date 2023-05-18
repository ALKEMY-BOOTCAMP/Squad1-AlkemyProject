from django.contrib import admin
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')
    search_fields = ('nombre',) #Busqueda por nombre
    list_filter = ('activo',)

admin.site.register(Servicio, ServicioAdmin)
