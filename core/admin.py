from django.contrib import admin
from .models import Horario

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['materia', 'maestro', 'salon', 'dia', 'hora_inicio', 'hora_fin', 'turno', 'grupo']
    list_filter = ['dia', 'turno', 'grupo']
    search_fields = ['materia', 'maestro', 'salon']
