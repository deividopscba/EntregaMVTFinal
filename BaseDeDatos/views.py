from django.shortcuts import render
from django.http import HttpResponse
from BaseDeDatos.models import Paciente, Medico, HistoriaClinica
from BaseDeDatos.forms import form_pacientes, form_medicos, form_historiaclinica

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def api_pacientes(request):
    if request.method == "POST":
        formulario = form_pacientes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            paciente = Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], 
                fechadenacimiento=informacion['fechadenacimiento'], id=informacion['id'], direccion=informacion['direccion'], 
                ciudad=informacion['ciudad'], email=informacion['email'])
            paciente.save()
            return render(request, "inicio.html")
    else:
        formulario=form_pacientes()
    return render(request, "api_pacientes.html", {"formulario": formulario})

def buscar_paciente(request):
    if request.GET["id"]:
        id = request.GET["id"]
        pacientes = Paciente.objects.filter(id__icontains = id)
        return render(request, "buscar_pacientes.html", {"pacientes":pacientes})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def api_medicos(request):
    if request.method == "POST":
        formulario = form_medicos(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            medico = Medico(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], 
                fechadenacimiento=informacion['fechadenacimiento'], id=informacion['id'], direccion=informacion['direccion'], 
                ciudad=informacion['ciudad'], email=informacion['email'], profesion=informacion['profesion'])
            medico.save()
            return render(request, "inicio.html")
    else:
        formulario=form_medicos()
    return render(request, "api_medicos.html", {"formulario": formulario})

def buscar_medico(request):
    if request.GET["id"]:
        id = request.GET["id"]
        medicos = Medico.objects.filter(id__icontains = id)
        return render(request, "buscar_medicos.html", {"medicos":medicos})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def api_HistoriasClinica(request):
    if request.method == "POST":
        formulario = form_historiaclinica(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            historia = HistoriaClinica( id_historia = informacion['id_historia'], nombre_pac = informacion['nombre_pac'], apellido_pac = informacion['apellido_pac'], fecha_hist = informacion['fecha_hist'], diagnostico = informacion['diagnostico'] )
            historia.save()
            return render(request, "api_HistoriasClinica.html")
    else:
        formulario = form_historiaclinica()
        return render(request, "api_HistoriasClinica.html", {"formulario": formulario})