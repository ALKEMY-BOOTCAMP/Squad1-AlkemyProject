from django.urls import path
from reservas.views import actualizar_empleado, listar_empleados, crear_empleado, borrar_empleado, registrar_coordinador



app_name = 'reservas'

urlpatterns = [
    # Otras URLs de tu proyecto...
    path('', listar_empleados, name='listar_empleados'),
    path('modificar/<int:pk>', actualizar_empleado, name='actualizar_empleado'),
    path('borrar/<int:pk>',borrar_empleado, name='borrar_empleado'),
    path('crear/<int:pk>', crear_empleado, name='crear_empleado'),
    path('coordinadores/nuevo/', registrar_coordinador, name='registrar_coordinador'),
]
