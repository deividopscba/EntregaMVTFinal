from django.urls import path
from BaseDeDatos.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('pacientes/', Pacientes),
    path('medicos/', Medicos),
]