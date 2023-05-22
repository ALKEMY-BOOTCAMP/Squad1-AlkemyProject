from django.urls import path
from reservas.views import actualizar_empleado,listar_empleados, crear_empleado


app_name = 'reservas'

urlpatterns = [
    # Otras URLs de tu proyecto...
    path('', listar_empleados, name='listar_empleados'),
    path('modificar/<int:id>/', actualizar_empleado, name='actualizar_empleado'),
    path('crear/', crear_empleado, name='crear_empleado'), 
]
