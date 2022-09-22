from django.shortcuts import render
from django.http import HttpResponse
from BaseDeDatos.models import Paciente, Medico
from BaseDeDatos.forms import form_pacientes, form_medicos

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def pacientes(request):
    if request.method == "POST":
        paciente = Paciente(nombre = request.POST['nombre'], apellido=request.POST['apellido'], edad=request.POST['edad'], fechadenacimiento=request.POST['fechadenacimiento'], id=request.POST['id'], direccion=request.POST['direccion'],ciudad=request.POST['ciudad'], email=request.POST['email'])
        paciente.save()
        return render(request, "inicio.html")
    return render(request, 'pacientes.html')



def api_pacientes(request):
    if request.method == "POST":
        formulario = form_pacientes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            paciente = Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'],fechadenacimiento=informacion['fechadenacimiento'], id=informacion['id'], direccion=informacion['direccion'], ciudad=informacion['ciudad'], email=informacion['email'])
            paciente.save()
            return render(request, "api_pacientes.html")
    else:
        formulario=form_pacientes()
    return render(request, "api_pacientes.html", {"formulario": formulario})

def buscar_paciente(request):
    if request.GET["id"]:
        id = request.GET["id"]
        pacientes = Paciente.objects.filter(id__icontains = id)
        return render(request, "pacientes.html", {"pacientes":pacientes})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def medicos(request):
    if request.method == "POST":
        formulario = form_medicos(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            medico = Medico(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], 
                fechadenacimiento=informacion['fechadenacimiento'], id=informacion['id'], direccion=informacion['direccion'], 
                ciudad=informacion['ciudad'], email=informacion['email'], profesion=informacion['profesion'])
            medico.save()
            return render(request, "medicos.html")
    else:
        formulario=form_medicos()
    return render(request, "medicos.html", {"formulario": formulario})