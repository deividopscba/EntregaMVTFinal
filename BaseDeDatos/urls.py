from django.urls import path
from BaseDeDatos.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio),
    path('api_pacientes/', api_pacientes),
    path('api_medicos/', api_medicos),
    path('buscar_medico/', buscar_medico),
    path('api_HistoriasClinica/',api_HistoriasClinica),
    path('buscar_paciente/',buscar_paciente),
    path('login/', login_request),
    path('registro/', registro),
    path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name="Logout" ),


]