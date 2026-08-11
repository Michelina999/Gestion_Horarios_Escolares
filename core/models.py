from django.db import models

DIAS_SEMANA = [
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sábado', 'Sábado'),
]

TURNOS = [
    ('Matutino', 'Matutino'),
    ('Vespertino', 'Vespertino'),
    ('Nocturno', 'Nocturno'),
]

class Horario(models.Model):
    materia = models.CharField(max_length=100, verbose_name='Materia')
    maestro = models.CharField(max_length=100, verbose_name='Maestro')
    salon = models.CharField(max_length=50, verbose_name='Salón')
    dia = models.CharField(max_length=20, choices=DIAS_SEMANA, verbose_name='Día')
    hora_inicio = models.TimeField(verbose_name='Hora de inicio')
    hora_fin = models.TimeField(verbose_name='Hora de fin')
    turno = models.CharField(max_length=20, choices=TURNOS, verbose_name='Turno')
    grupo = models.CharField(max_length=20, verbose_name='Grupo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.materia} - {self.dia} {self.hora_inicio}"

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['dia', 'hora_inicio']
