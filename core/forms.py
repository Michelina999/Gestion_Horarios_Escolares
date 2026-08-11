from django import forms
from .models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['materia', 'maestro', 'salon', 'dia', 'hora_inicio', 'hora_fin', 'turno', 'grupo']
        widgets = {
            'materia': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej: Matemáticas'}),
            'maestro': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nombre del maestro'}),
            'salon': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej: Aula 101'}),
            'dia': forms.Select(attrs={'class': 'form-select'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'turno': forms.Select(attrs={'class': 'form-select'}),
            'grupo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej: 3°A'}),
        }
