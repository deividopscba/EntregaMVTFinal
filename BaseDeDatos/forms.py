from django import forms

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
