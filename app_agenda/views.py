from django.shortcuts import render
from .models import Usuario
# Create your views here
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.sobrenome = request.POST.get('sobrenome')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()

    #Exibir todos os usuarios ja cadastrados no banco de dados em uma pagina.
    usuarios = {
        'usuarios': Usuario.objects.all()
    }


    #Rotornando os dados para pagina de listagem de ususarios
    return render(request,'usuarios/usuarios.html',usuarios)
