from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from .models import Empleado


#funcion que por busqueda de id activa un empleado y muestra un mensaje por ahora
def activar_empleado(request,id):
    empleado = get_object_or_404(Empleado, id = pk)
    empleado.activo = True
    empleado.save()
    
    print("Activado")
    