from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eliminar/<int:pk>/', views.eliminar_horario, name='eliminar_horario'),
]
