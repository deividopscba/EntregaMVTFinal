from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_pacientes(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fechadenacimiento = forms.DateField()
    id = forms.IntegerField()
    direccion = forms.CharField(max_length=40)
    ciudad = forms.CharField(max_length=40)
    email = forms.EmailField()

class form_medicos(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fechadenacimiento = forms.DateField()
    id = forms.IntegerField()
    direccion = forms.CharField(max_length=40)
    ciudad = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)

class form_historiaclinica(forms.Form):
    id_historia = forms.IntegerField()
    nombre_pac = forms.CharField(max_length=40)
    apellido_pac = forms.CharField(max_length=40)
    fecha_hist = forms.DateField()
    diagnostico = forms.CharField(max_length=200)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2: forms.CharField(label="Repetir Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}