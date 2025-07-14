from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def perfil_view(request):
    return render(request, 'perfil.html')

def editar_perfil_view(request):
    return render(request, 'editar-perfil.html')

