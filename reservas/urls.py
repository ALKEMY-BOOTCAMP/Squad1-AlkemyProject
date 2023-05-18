from django.urls import path
#from .views import

app_name = 'reservas'

url_patters = [
   #URLS DEL MODELO EMPLEADO
   path('/empleados/activar/<int: id>', activar_empleado, name="activar_empleado"),
]