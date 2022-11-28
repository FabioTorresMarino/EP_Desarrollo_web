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
        codigo_usuario = request.POST.get('codigo_usuario')
        clave = request.POST.get('clave')
        print('El nombre del usuario es: ' + str(nombre))
        print('El apellido del usuario es: ' + str(apellido))
        print('El codigo de usuario es: ' + str(codigo_usuario))
        print('La clave de usuario es: ' + str(clave))
        nuevoUsuario.append(str(nombre))
        nuevoUsuario.append(str(apellido))
        nuevoUsuario.append(str(codigo_usuario))
        nuevoUsuario.append(str(clave))
        usuario(nombre=str(nombre),apellido=str(apellido),codigo_usuario=str(codigo_usuario),clave=str(clave)).save()
    return render(request,'project_parcial/login.html',{
        'usuarios': usuario.objects.all(),
    })
def dashboard(request):
    return render(request,'')
def view_tareas(request):
    return  render(request,'')

