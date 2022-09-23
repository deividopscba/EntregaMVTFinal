from django.http import HttpResponse

def inicio(request):
    return HttpResponse(f'Hola soy Inicio de MVT')