from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(HistoriaClinica)
