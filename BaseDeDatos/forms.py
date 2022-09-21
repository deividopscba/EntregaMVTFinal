from django import forms

class form_pacientes(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    fechadenacimiento = forms.DateField()
    id = forms.IntegerField()
    direccion = forms.CharField()
    ciudad = forms.CharField()
    email = forms.EmailField()

class form_medicos(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    fechadenacimiento = forms.DateField()
    id = forms.IntegerField()
    direccion = forms.CharField()
    ciudad = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField