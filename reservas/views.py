from django.shortcuts import render, get_object_or_404 , redirect
from .models import Empleado, Coordinador
from .forms import EmpleadoForm, CoordinadorForm


def listar_empleados(request):
    lista_empleados = Empleado.objects.all()
    
    return render(request, 'registro_empleados.html', {
        'titulo':'LISTADO DE Empleados',
        'empleados': lista_empleados,
        
    })

def actualizar_empleado(request, pk):
    
    empleado = Empleado.objects.get(id=pk)
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('/empleados/')  # Redireccionar a la página de empleados después de actualizar
    else:
        form = EmpleadoForm(instance=empleado)
    
    return render(request, 'actualizar_empleado.html', {'form': form})


def crear_empleado(request, pk):
    
    empleado = Empleado.objects.get(id=pk)
    
    if request.method == 'POST':
        # Si el formulario fue enviado (POST request), procesarlo
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            # El formulario es válido, procesar los datos
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            numero_de_legajo = form.cleaned_data['numero_de_legajo']
            activo = form.cleaned_data['activo']
            form.save()
            return redirect('/empleados/')
            # Aquí puedes realizar acciones con los datos, como guardarlos en la base de datos

            # Redirigir a una página de éxito o hacer otra cosa después de procesar el formulario
    else:
        # Si el formulario no fue enviado (GET request), crear una instancia del formulario vacío
        form = EmpleadoForm()
    
    return render(request, 'crear_empleado.html', {'form': form})

def borrar_empleado(request, pk):
    empleado_a_borrar = get_object_or_404(Empleado, pk=pk)
    empleado_a_borrar.delete()
    return redirect('/empleados/')


def activar_empleado(request,pk):
    empleado_a_activar = get_object_or_404(Empleado, pk=pk)
    empleado_a_activar .delete()
    return redirect('/empleados/')


def registrar_coordinador(request):
    if request.method == 'POST':
        # Si el formulario fue enviado (POST request), procesarlo
        form = CoordinadorForm(request.POST)
        if form.is_valid():
            # El formulario es válido, procesar los datos
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            numero_documento = form.cleaned_data['numero_documento']
            activo = form.cleaned_data['activo']
            form.save()
            return redirect('/empleados/coordinadores/')
            # Aquí puedes realizar acciones con los datos, como guardarlos en la base de datos

            # Redirigir a una página de éxito o hacer otra cosa después de procesar el formulario
    else:
        # Si el formulario no fue enviado (GET request), crear una instancia del formulario vacío
        form = CoordinadorForm()
    
    return render(request, 'registrar_coordinador.html', {'form': form})

def listar_coordinadores(request):
    lista_coordinadores = Coordinador.objects.all()
    
    return render(request, 'registro_coordinadores.html', {
        'titulo':'LISTADO DE CORDINADORES',
        'coordinadores': lista_coordinadores,
        
    })


def activar_desactivar_coordinador(request, pk):
    coordinador = get_object_or_404(Coordinador, id=pk)

    if request.method == 'POST':
        activo = request.POST.get('activo')
        if activo:
            coordinador.activo = True
            print("coordinador activado")
        else:
            coordinador.activo = False
            print("coordinador desactivado")
        coordinador.save()
        return redirect('/empleados/coordinadores/')  # Redirecciona a la página deseada después de guardar

    return render(request, 'registro_coordinadores.html', {'coordinador': coordinador})
