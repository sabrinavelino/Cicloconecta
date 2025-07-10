
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
    path('novo-anuncio/', views.novo_anuncio, name='novo_anuncio'),
    path('usuarios/', include('usuarios.urls')),  
]
