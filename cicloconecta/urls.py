
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('gabinete/', views.gabinete, name='gabinete'),
    path('hd/', views.hd, name='hd'),
    path('memoria/', views.memoria, name='memoria'),
    path('meus-anuncios/', views.meus_anuncios, name='meus_anuncios'),
    path('perifericos/', views.perifericos, name='perifericos'),
    path('novo_anuncio/', views.novo_anuncio, name='novo_anuncio'),
    path('suporte_manutencao/', views.suporte_manutencao, name='suporte_manutencao'),
    path('pontos_de_coleta/', views.pontos_de_coleta, name='pontos_de_coleta'),
    path('usuarios/', include('usuarios.urls')),  
]


