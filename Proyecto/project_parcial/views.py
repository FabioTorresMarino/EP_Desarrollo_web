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
        usuario_solicitante = []
        nombre = request.POST.get('nombreUsuario')
        clave = request.POST.get('clave')
        usuario_solicitante.append(str(nombre))
        usuario_solicitante.append(str(clave))
        usuario(nombre=str(nombre),clave=str(clave)).save()
    return render(request,'project_parcial/login.html',{
        'usuarios': usuario.objects.all(),
    })
def dashboard(request):
    return render(request,'project_parcial/dashboard.html')
def view_tareas(request):
    return  render(request,'project_parcial/view_tareas.html')
def register_user(request):
    if request.method == 'POST':
        nuevoUsuario = []
        nombre = request.POST.get('nombreUsuario')
        apellido = request.POST.get('apellidoUsuario')
        codigo_usuario = request.POST.get('codigo_usuario')
        clave = request.POST.get('clave')
        nuevoUsuario.append(str(nombre))
        nuevoUsuario.append(str(apellido))
        nuevoUsuario.append(str(codigo_usuario))
        nuevoUsuario.append(str(clave))
        usuario(nombre=str(nombre),apellido=str(apellido),codigo_usuario=str(codigo_usuario),clave=str(clave)).save()
    return render(request,'project_parcial/register_user.html',{
        'usuarios': usuario.objects.all(),
    })


