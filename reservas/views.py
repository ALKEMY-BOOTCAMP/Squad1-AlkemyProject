from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .forms import EmpleadosForm
from .models import Empleado


# Create your views here.

#Vista del formulario para actualizar el registro de un empleado
def empleados_form_view(request, pk):
    
    empleado = get_object_or_404(Empleado, id=pk)  # Obtener el objeto Empleado correspondiente al ID proporcionado
    form = EmpleadosForm(instance=empleado)  # Crear una instancia del formulario EmpleadosForm con los datos del empleado
    
    if request.method == 'POST':
        form = EmpleadosForm(request.POST)  # Crear una instancia del formulario EmpleadosForm con los datos del formulario enviado
        if form.is_valid():  # Verificar si el formulario es válido
            form.save()  # Guardar los datos del formulario en la base de datos
            return redirect('base.html')  # Redireccionar a una página específica después de guardar los datos
    else:
        form = EmpleadosForm()  # Crear una instancia vacía del formulario EmpleadosForm si no se envió ningún formulario
    
    return render(request, 'empleados/empleados_form.html', {'form': form})  # Renderizar el formulario en la plantilla 'empleados/empleados_form.html'

# Vista para listar el registro de empleados
def empleados_listado(request):
    empleados = empleados.object.All()  # Obtener todos los objetos de la clase Empleado
    
    return render(request, 'listar_empleados.html', {'titulo': 'Lista De Empleados', 'empleados': empleados})
    # Renderizar la plantilla 'listar_empleados.html', pasando el título y la lista de empleados como contexto

# Vista para crear un nuevo empleado
def empleados_nuevo(request):
    
    if request.method == 'POST':
        form = EmpleadosForm(request.POST)  # Crear una instancia del formulario EmpleadosForm con los datos enviados en la solicitud POST
        if form.is_valid():  # Verificar si el formulario es válido
            form.save()  # Guardar los datos del formulario en la base de datos
            return redirect('listar_empleados.html')  # Redireccionar a la página de listado de empleados
    else:
        form = EmpleadosForm()  # Crear una instancia vacía del formulario EmpleadosForm si la solicitud no es de tipo POST
    
    return render(request, 'empleados_nuevo.html', {'form': form})
    # Renderizar la plantilla 'empleados_nuevo.html', pasando el formulario como contexto