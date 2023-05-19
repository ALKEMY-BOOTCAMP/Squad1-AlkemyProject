from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from .models import Empleado
from .empleado_forms import EmpleadoForm


#Funcion que por busqueda de id activa un empleado y muestra un mensaje por ahora
def activar_empleado(request,id):
    empleado = get_object_or_404(Empleado, id = pk)
    empleado.activo = True
    empleado.save()
    
    print("Activado")
    
#Funcion que por busqueda de id desactiva un empleado y muestra un mensaje por ahora
def desactivar_empleado(request,id):
    empleado = get_object_or_404(Empleado, id = pk)
    empleado.activo = False
    empleado.save()
    
    print("Desactivado")
    

#View para registrar empleado que pide que el metodo del request sea POST
def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario y guardar el nuevo empleado
            # redireccionar a una página de éxito o realizar cualquier acción necesaria
            return redirect('exito')
    else:
        #Form vacio 
        form = EmpleadoForm()

    #Implemantar los templates
    #return render(request, 'registro_empleado.html', {'form': form})

    