from django import forms
from .models import Empleado, Coordinador

from django import forms

from .models import *

class EmpleadoForm(forms.ModelForm):
    
    # Especifica que el formulario está asociado con el modelo empleado
    class Meta:
        model = Empleado
        
        # Enumera los campos del modelo Empleado que se incluirán en el formulario.
        fields = [
            'nombre',
            'apellido',
            'numero_de_legajo',
            'activo',
        ]
        
        # Proporciona etiquetas legibles por humanos para los campos del formulario.
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'numero_de_legajo': 'Numero De Legajo',
            'activo': 'Activo',
        }
        
        # Epecifica los widgets de entrada HTML que se utilizarán para cada campo del 
        # formulario. En este caso, los campos del formulario se representan como widgets TextInput 
        # o IntegerField con la clase CSS form-control aplicada.
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_de_legajo': forms.NumberInput(attrs={'class': 'form-control'}),
            'Activo': forms.BooleanField(),
        }

class CoordinadorForm(forms.ModelForm):
    class Meta:
        model = Coordinador
        fields = '__all__'
