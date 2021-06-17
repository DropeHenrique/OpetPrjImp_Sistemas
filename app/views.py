from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def cadastrar(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})
    return (print "aguardando aprovação")

def logar(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('fimdatela')
        else:
            return HttpResponse('<h1> usuario ou senha invalido </h1>')
            form_login = AuthenticationForm('Usuário ou Senha Inválido')
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login} )


def index(request):
    return render(request, 'index.html')

def fimdatela(request):
    return render(request, 'fimdatela.html')
