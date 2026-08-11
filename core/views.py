from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import HorarioForm
from .models import Horario

def index(request):
    horarios = Horario.objects.all()
    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Horario registrado exitosamente!')
            return redirect('index')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = HorarioForm()

    return render(request, 'core/index.html', {'form': form, 'horarios': horarios})

def eliminar_horario(request, pk):
    horario = get_object_or_404(Horario, pk=pk)
    if request.method == 'POST':
        horario.delete()
        messages.success(request, 'Horario eliminado.')
    return redirect('index')
