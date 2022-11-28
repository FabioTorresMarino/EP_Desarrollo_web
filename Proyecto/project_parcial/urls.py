from . import views
from django.urls import path

app_name = 'project_parcial'

urlpatterns =[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register_user',views.register_user,name='register_user'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('view_tareas',views.view_tareas,name='view_tareas'),
]