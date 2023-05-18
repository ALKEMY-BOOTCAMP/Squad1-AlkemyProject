from django.contrib import admin
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')
    list_search = ('nombre',)
    list_filter = ('activo',)

admin.site.register(Servicio, ServicioAdmin)
