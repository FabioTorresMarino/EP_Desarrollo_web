from django.shortcuts import render
from django.http import HttpResponse

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
        edad = request.POST.get('edadUsuario')
        print('El nombre del usuario es: ' + str(nombre))
        print('El apellido del usuario es: ' + str(apellido))
        print('La edad del usuario es: ' + str(edad))
        nuevoUsuario.append(str(nombre))
        nuevoUsuario.append(str(apellido))
        nuevoUsuario.append(str(edad))
        lista_usuarios.append(nuevoUsuario)
    return render(request,'project_parcial/login.html',{
        'usuarios': lista_usuarios,
    })
def dashboard(request):
    return render(request,'')
def view_tareas(request):
    return  render(request,'')
    
