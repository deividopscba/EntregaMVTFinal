from django.shortcuts import render, redirect
from django.http import HttpResponse
from BaseDeDatos.models import Paciente, Medico, HistoriaClinica
from BaseDeDatos.forms import form_pacientes, form_medicos, form_historiaclinica, UserRegisterForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate 

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def inicio(request):
    return render(request, "inicio.html")
@login_required
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
@login_required
def buscar_paciente(request):
    if request.GET["id"]:
        id = request.GET["id"]
        pacientes = Paciente.objects.filter(id__icontains = id)
        return render(request, "buscar_pacientes.html", {"pacientes":pacientes})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
@login_required
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
@login_required
def buscar_medico(request):
    if request.GET["id"]:
        id = request.GET["id"]
        medicos = Medico.objects.filter(id__icontains = id)
        return render(request, "buscar_medicos.html", {"medicos":medicos})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
@login_required
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


def login_request(request):
   if request.method == 'POST':
      form = AuthenticationForm(request, data = request.POST)
      if form.is_valid():
         user = form.cleaned_data.get('username')
         pwd = form.cleaned_data.get('password')

         user = authenticate(username = user, password = pwd)

         if user is not None:
            login(request, user)
            return render(request, "inicio.html")
         else:
            return render (request, "login.html", {'form':form})
      else:
         return render (request, "login.html", {'form':form})    

   form = AuthenticationForm()
   return render(request, 'login.html', {'form' : form})

def registro(request):
   if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect("/BaseDeDatos/login/")
   else:
      form = UserRegisterForm()
      return render(request, 'registro.html', {'form':form})

def about(request):
    return render(request, "about.html")

def create_pacientes(request):
    if request.method == 'POST':
        paciente = Paciente(nombre = request.POST['nombre'], apellido = request.POST['apellido'], edad = request.POST['edad'],
        fechadenacimiento = request.POST['fechadenacimiento'], id = request.POST['id'], direccion = request.POST['direccion'],
        ciudad = request.POST['ciudad'], email = request.POST['email'])
        paciente.save()
        pacientes = Paciente.objects.all()
        return render(request, "CRUD/read_pacientes.html", {"pacientes": pacientes})
    return render(request, "CRUD/create_pacientes.html")

def read_pacientes(request=None):
    pacientes = Paciente.objects.all()
    return render(request, "CRUD/read_pacientes.html", {"pacientes": pacientes})

def update_pacientes(request, paciente_id):
    paciente = Paciente.objects.get(id = paciente_id)

    if request.method == 'POST':
        formulario = form_pacientes(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            paciente.nombre = informacion['nombre']
            paciente.apellido = informacion['apellido']
            paciente.edad = informacion['edad']
            paciente.fechadenacimiento = informacion['fechadenacimiento']
            paciente.id = informacion['id']
            paciente.direccion= informacion['direccion']
            paciente.ciudad = informacion['ciudad']
            paciente.email = informacion['email']
            paciente.save()
            pacientes = Paciente.objects.all()
            return render(request, "CRUD/read_pacientes.html", {"pacientes": pacientes})
    else:
        formulario = form_pacientes(initial={'nombre': paciente.nombre, 'apellido': paciente.apellido, 'edad': paciente.edad,
        'fechadenacimiento': paciente.fechadenacimiento, 'id': paciente.id, 'direccion': paciente.direccion,
        'ciudad': paciente.ciudad,'email': paciente.email})
    return render(request,"CRUD/update_pacientes.html", {"formulario": formulario})

def delete_pacientes(request, paciente_id):
    paciente = Paciente.objects.get(id =  paciente_id)
    paciente.delete()

    pacientes = Paciente.objects.all()    
    return render(request, "CRUD/read_pacientes.html", {"pacientes": pacientes})
