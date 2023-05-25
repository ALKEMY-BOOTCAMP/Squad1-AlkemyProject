from django import forms

from .models import *

class EmpleadosForm(forms.ModelForm):
    
    # Especifica que el formulario está asociado con el modelo empleado
    class Meta:
        model = Empleado
        
        # Enumera los campos del modelo Empleado que se incluirán en el formulario.
        fields = [
            'nombre',
            'apellido',
            'numero_legajo',
        ]
        
        # Proporciona etiquetas legibles por humanos para los campos del formulario.
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'numero_legajo': 'Numero De Legajo',
        }
        
        # Epecifica los widgets de entrada HTML que se utilizarán para cada campo del 
        # formulario. En este caso, los campos del formulario se representan como widgets TextInput 
        # o IntegerField con la clase CSS form-control aplicada.
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_legajo' : forms.IntegerField(attrs={'class': 'form-control'}),
        }
        
class CoordinadorForm(forms.ModelForm):
    
    class Meta:
        model = Coordinador
    
        fields = [
            'nombre',
            'apellido',
            'numero_documento',
            'activo',
        ]
    
        labels = {
            'Nombre': 'nombre',
            'Apellido': 'apellido',
            'DNI': 'numero_documento',
            'Acctivo': 'acctivo',
        }
    
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento' : forms.IntegerField(attrs={'class': 'form-control'}),
            'activo': forms.BooleanField(attrs={'class': 'form-control'})
        }