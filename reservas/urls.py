from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    # Otras URLs de tu proyecto...
    path('empleados/modificar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
]