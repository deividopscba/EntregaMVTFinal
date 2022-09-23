from django.urls import path
from BaseDeDatos.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('api_pacientes/', api_pacientes),
    path('api_medicos/', api_medicos),
    path('buscar_medico/', buscar_medico),
    path('api_HistoriasClinica/',api_HistoriasClinica)
]