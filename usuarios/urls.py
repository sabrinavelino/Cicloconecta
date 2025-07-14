from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('editar-perfil/', views.editar_perfil_view, name='editar_perfil'),
]
    