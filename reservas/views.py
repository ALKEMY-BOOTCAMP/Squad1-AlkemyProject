from django.shortcuts import render, redirect
from .models import Empleado
from .forms import EmpleadoForm

def actualizar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados')  # Redireccionar a la página de empleados después de actualizar
    else:
        form = EmpleadoForm(instance=empleado)
    
    return render(request, 'actualizar_empleado.html', {'form': form})

