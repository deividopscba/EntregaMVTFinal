from django.http import HttpResponse
from django.template import loader

def inicio(self):
    planilla = loader.get_template ("inicio.html")
    doc = planilla.render()
    return HttpResponse(doc)

def Pacientes(self):
    planilla = loader.get_template ("pacientes.html")
    doc = planilla.render()
    return HttpResponse(doc)