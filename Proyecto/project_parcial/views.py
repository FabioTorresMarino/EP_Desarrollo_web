from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario
from .models import tarea 

# Create your views here.
lista_usuarios = [['Fabio','Torres','20'],['Cristiano','Ronaldo','37'],['Lionel','Messi','35']]

def index(request):
    return HttpResponse('Esta es mi primera vista')

def login(request):
    if request.method == 'POST':
        nuevoUsuario = []
        print('Hola se ha posteado información')
        nombre = request.POST.get('nombreUsuario')
        apellido = request.POST.get('apellidoUsuario')
        codigoUsuario = request.POST.get('codigoUsuario')
        print('El nombre del usuario es: ' + str(nombre))
        print('El apellido del usuario es: ' + str(apellido))
        print('El codigo de usuario es: ' + str(codigoUsuario))
        nuevoUsuario.append(str(nombre))
        nuevoUsuario.append(str(apellido))
        nuevoUsuario.append(str(codigoUsuario))
    return render(request,'project_parcial/login.html',{
        'usuarios': usuario.objects.all(),
    })
def dashboard(request):
    return render(request,'')
def view_tareas(request):
    return  render(request,'')

