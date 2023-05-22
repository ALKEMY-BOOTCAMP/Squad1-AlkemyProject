from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import EmpleadosForm
from .models import Empleado


# Create your views here.
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
