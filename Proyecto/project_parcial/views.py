from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Esta es mi primera vista')

def login(request):
    lista_usuarios = [['Fabio','Torres','20'],['Cristiano','Ronaldo','37'],['Lionel','Messi','35']]
    return render(request,'project_parcial/login.html',{
        'usuarios': lista_usuarios,
    })