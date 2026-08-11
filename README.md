# Gestión de Horarios Escolares

Aplicación web desarrollada con **Django** para la gestión y administración de horarios escolares.

El sistema permite registrar, consultar y eliminar horarios académicos, organizando información como materias, maestros, salones, grupos, días de la semana, turnos y horas de clase.

---


### Página principal

![Página principal]

### Registro de horario

![Registro de horario]

### Horarios registrados

![Horarios registrados]

---

## Tecnologías utilizadas

- Python
- Django 5.2.15
- SQLite
- HTML
- Django Templates
- Git
  GitHub

---

##  Funcionalidades

El sistema permite:

- ✅ Registrar horarios escolares.
- ✅ Consultar horarios registrados.
- ✅ Registrar materias.
- ✅ Registrar maestros.
- ✅ Registrar salones.
- ✅ Registrar grupos.
- ✅ Seleccionar el día de la semana.
- ✅ Seleccionar el turno.
- ✅ Definir hora de inicio.
- ✅ Definir hora de fin.
- ✅ Eliminar horarios.
- ✅ Mostrar mensajes de confirmación.
- ✅ Mostrar mensajes de error.
- ✅ Administrar la información mediante Django.

---

## Estructura del proyecto

```text
Gestion_Horarios_Escolares/
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── index.html
│   │       └── login.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── mi_proyecto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── screenshots/
│   ├── inicio.png
│   ├── registro.png
│   └── horarios.png
│
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
