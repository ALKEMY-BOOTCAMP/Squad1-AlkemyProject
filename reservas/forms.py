from django import forms
from .models import Empleado, Coordinador

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class CoordinadorForm(forms.ModelForm):
    class Meta:
        model = Coordinador
        fields = '__all__'
