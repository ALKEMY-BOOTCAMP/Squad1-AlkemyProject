from django.shortcuts import render, redirect
from .models import Empleado
from .forms import EmpleadoForm


def listar_empleados(request):
    lista_empleados = Empleado.objects.all()
    
    return render(request, 'registro_empleados.html', {
        'titulo':'LISTADO DE Empleados',
        'empleados': lista_empleados,
        
    })

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


def crear_empleado(request):
    if request.method == 'POST':
        # Si el formulario fue enviado (POST request), procesarlo
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            # El formulario es válido, procesar los datos
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            numero_legajo = form.cleaned_data['numero_legajo']
            # Aquí puedes realizar acciones con los datos, como guardarlos en la base de datos

            # Redirigir a una página de éxito o hacer otra cosa después de procesar el formulario
    else:
        # Si el formulario no fue enviado (GET request), crear una instancia del formulario vacío
        form = EmpleadoForm()

    return render(request, 'crear_empleado.html', {'form': form})
