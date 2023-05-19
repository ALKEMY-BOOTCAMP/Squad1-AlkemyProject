from django.urls import path
from .views import activar_empleado, desactivar_empleado

app_name = 'reservas'

url_patters = [
   #URLS DEL MODELO EMPLEADO
   path('/empleados/activar/<int: id>', activar_empleado, name="activar_empleado"),
   path('/empleados/desactivar/<int: id>', desactivar_empleado, name="desactivar_empleado"),
]