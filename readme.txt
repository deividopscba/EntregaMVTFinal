Guia de uso para la historia clinica electronica.
(Si queres entrar al admin a ver la base de datos te dejo un usuario y contraseña
user: andres
pass:ciecho65
)
Ingresar y buscar paciente:

1)Una vez hecho el python manage.py runserver la aplicacion te abre el inicio.html

2)Dirigirse a "Pacientes" para registrar un paciente.

3)Completar el formulario.

4)Volver a dirigirse a "Pacientes" y usar el buscardor de IDs.
(Algunos IDs ya registadros 1,2,3,4)

Ingresar y buscar medico:

1)Desde cualquier html dirigirse a "Medicos".

2)Completar el formulario.

3)Volver a dirigirse a "Medicos" y usar el buscador de IDs.

Ingresar una historia clinica:

1)Desde cualquier html dirigirse a "Historias clinicas".

2)Completar el formulario.

(Vale aclarar que este model lo hicimos para cumplir con la consigna que decia que tenian que ser 3 modelos.
 Es por eso que no le hicimos un form para buscar historias clinicas.
 Nuestra idea original era que la parte de historia clinica sea parte del paciente y del medico que trata a ese paciente,
 asi uno podria buscar por ID y que salgal todos los datos del paciente, quien lo trata y su historia clinica con las fechas de las evoluciones)