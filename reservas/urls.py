from django.urls import path
from reservas.views import actualizar_empleado, listar_empleados, crear_empleado, borrar_empleado, registrar_coordinador, listar_coordinadores, activar_desactivar_coordinador, crear_cliente,listar_clientes, crear_servicio, listar_servicios, borrar_servicio


app_name = 'reservas'

urlpatterns = [
    # Otras URLs de tu proyecto...
    path('', listar_empleados, name='listar_empleados'),
    path('modificar/<int:pk>', actualizar_empleado, name='actualizar_empleado'),
    path('borrar/<int:pk>', borrar_empleado, name='borrar_empleado'),
    path('crear/<int:pk>', crear_empleado, name='crear_empleado'),

    path('coordinadores/', listar_coordinadores, name='listar_coordinadores'),
    path('coordinadores/nuevo/', registrar_coordinador,
         name='registrar_coordinador'),
    path('coordinadores/activar/<int:pk>', activar_desactivar_coordinador,
         name='activar_desactivar_coordinador'),

    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/nuevo/', crear_cliente, name='crear_cliente'),
    
    path('servicios/', listar_servicios, name='listar_servicios'),
    path('servicios/nuevo/', crear_servicio, name='crear_servicio'),
    path('borrar-servicio/<int:pk>', borrar_servicio, name='borrar_servicio'),
    
    
    
    

]
