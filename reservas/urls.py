from django.urls import path
#from .views import
from .views import empleados_form_view, empleados_listado

app_name = 'reservas'

url_patters = [
   # path()
   path('empleados/modificar/<int:numero_legajo>', empleados_form_view, name='empleados_form_view'),
   path('/empleados/listado', empleados_listado, name='empleados_listado'),
]