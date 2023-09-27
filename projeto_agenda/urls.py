from django.urls import path
from app_agenda import views

urlpatterns = [

    #rota, view , nome de referencia
    path('', views.home,name='home'),


    #enviando para pagina usuarios.
    path('usuarios/', views.usuarios,name='listagem_usuarios'),


]
