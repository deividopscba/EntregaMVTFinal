from django.urls import path
from BaseDeDatos.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('pacientes/', pacientes),
    path('medicos/', medicos),
    path('api_pacientes/', api_pacientes)
]