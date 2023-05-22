from django.urls import path
#from .views import
from .views import empleados_form_view

app_name = 'reservas'

url_patters = [
   # path()
   path('actualizar/<int:numero_legajo>', empleados_form_view, name='empleados_form_view'),
]